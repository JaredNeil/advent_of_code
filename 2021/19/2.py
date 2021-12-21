from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import chain, combinations, permutations, product, repeat

import numpy as np
from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mapint, mul, pp, transpose, window_of

rotation_matricies = []
for x, y, z in permutations([0, 1, 2]):
    for sx, sy, sz in product([-1, 1], repeat=3):
        rotation_matrix = np.zeros((3, 3))
        rotation_matrix[0, x] = sx
        rotation_matrix[1, y] = sy
        rotation_matrix[2, z] = sz
        if np.linalg.det(rotation_matrix) == 1:
            rotation_matricies.append(rotation_matrix)

def rotate(pos, matrix):
    return tuple(mapint(np.matmul(matrix, pos)))

def rotations(pos):
    for rotation_matrix in rotation_matricies:
        yield rotate(pos, rotation_matrix)


(lines,) = load_lines(repeat(s))
scanners = {}
i = None
for line in lines:
    if line.startswith("---"):
        i = int(line.split()[2])
        scanners[i] = []
    else:
        scanners[i].append(tuple(mapint(line.split(","))))

def diff(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def norm_delta(a, b):
    d = diff(a, b)
    return min(chain(rotations(d), rotations((-d[0], -d[1], -d[2]))))

def find_rot(a, b):
    for i, r in enumerate(rotations(b)):
        if a == r:
            return i

deltas = {}
delta_map = {}
for s, beacons in scanners.items():
    deltas[s] = Counter()
    delta_map[s] = defaultdict(set)
    for a, b in combinations(beacons, 2):
        d  = norm_delta(a, b)
        delta_map[s][d].add(a)
        delta_map[s][d].add(b)
        deltas[s][d] += 1

matches = {}
for pair in combinations(deltas, 2):
    scan_a = min(pair)
    scan_b = max(pair)
    overlap = deltas[scan_a] & deltas[scan_b]
    matches[scan_a, scan_b] = overlap

overlapping = defaultdict(set)
for a, b in matches:
    count = sum(matches[a, b].values())
    if count >= 66:
        overlapping[a].add(b)
        overlapping[b].add(a)

scanner_rotations = {0: rotation_matricies[3]}
scanner_positions = {0: (0, 0, 0)}
todo = set([0])
while todo:
    this = todo.pop()
    for other in overlapping[this]:
        if other not in scanner_positions:
            todo.add(other)
            pair = (min(this, other), max(this, other))
            for delta in reversed(matches[pair]):
                this_a, this_b = delta_map[this][delta]
                this_a = rotate(this_a, scanner_rotations[this])
                this_a = add(this_a, scanner_positions[this])
                this_b = rotate(this_b, scanner_rotations[this])
                this_b = add(this_b, scanner_positions[this])
                this_diff = diff(this_a, this_b)
                other_a, other_b = delta_map[other][delta]
                other_diff = diff(other_a, other_b)
                rot_index = find_rot(this_diff, other_diff)
                if rot_index is not None:
                    scanner_rotations[other] = rotation_matricies[rot_index]
                    scanner_positions[other] = diff(this_a, rotate(other_a, scanner_rotations[other]))
                    break
                other_diff = diff(other_b, other_a)
                rot_index = find_rot(this_diff, other_diff)
                if rot_index is not None:
                    scanner_rotations[other] = rotation_matricies[rot_index]
                    scanner_positions[other] = diff(this_a, rotate(other_b, scanner_rotations[other]))
                    break
max_dist = 0
for a, b in combinations(scanners, 2):
    a0, a1, a2 = scanner_positions[a]
    b0, b1, b2 = scanner_positions[b]
    max_dist = max(max_dist, abs(a0-b0) + abs(a1-b1) + abs(a2-b2))
print(max_dist)