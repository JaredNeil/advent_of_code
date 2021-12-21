from collections import Counter, defaultdict
from itertools import chain, combinations, permutations, product, repeat
from typing import Dict, List, Set, Tuple

import numpy as np
from parse import line, load_lines, s
from util import mapint

V3 = Tuple[int, int, int]
ScannerId = int

rotation_matricies: List[np.ndarray] = []
for x, y, z in permutations([0, 1, 2]):
    for sx, sy, sz in product([-1, 1], repeat=3):
        rotation_matrix = np.zeros((3, 3))
        rotation_matrix[0, x] = sx
        rotation_matrix[1, y] = sy
        rotation_matrix[2, z] = sz
        if np.linalg.det(rotation_matrix) == 1:
            rotation_matricies.append(rotation_matrix)


def rotate(pos: V3, matrix: np.ndarray) -> V3:
    return tuple(mapint(np.matmul(matrix, pos)))


def rotations(pos: V3) -> V3:
    for rotation_matrix in rotation_matricies:
        yield rotate(pos, rotation_matrix)


def diff(a: V3, b: V3) -> V3:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def add(a: V3, b: V3) -> V3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def norm_delta(a: V3, b: V3) -> V3:
    d = diff(a, b)
    return min(chain(rotations(d), rotations((-d[0], -d[1], -d[2]))))


def find_rot(a: V3, b: V3) -> int:
    for i, r in enumerate(rotations(b)):
        if a == r:
            return i

start = time.perf_counter_ns()
(lines,) = load_lines(repeat(s))
# Read the input into the `scanners` dict
scanners: Dict[ScannerId, List[Tuple[int, int, int]]] = {}
i = None
for line in lines:
    if line.startswith("---"):
        i = int(line.split()[2])
        scanners[i] = []
    else:
        scanners[i].append(tuple(mapint(line.split(","))))

# Calculate a delta between each pair of beacons on every scanner.
# The delta is "normalized", so for any pair of beacons the delta will be the same, no matter the position or orientation of the scanner.
deltas: Dict[ScannerId, "Counter[V3]"] = {}
delta_map: Dict[ScannerId, Dict[V3, V3]] = {}
for s, beacons in scanners.items():
    deltas[s] = Counter()
    delta_map[s] = defaultdict(set)
    for a, b in combinations(beacons, 2):
        d = norm_delta(a, b)
        delta_map[s][d].add(a)
        delta_map[s][d].add(b)
        deltas[s][d] += 1

# For each pair of scanners, calculate the intersecion of the multiset of deltas.
matches: Dict[Tuple[ScannerId, ScannerId], "Counter[V3]"] = {}
for pair in combinations(deltas, 2):
    scan_a = min(pair)
    scan_b = max(pair)
    overlap = deltas[scan_a] & deltas[scan_b]
    matches[scan_a, scan_b] = overlap

# For each pair of scanners, count the total number of shared deltas.
# All scanners with 12 beacons in common will share at least 66 (12 choose 2) deltas.
overlapping: Dict[ScannerId, ScannerId] = defaultdict(set)
for a, b in matches:
    count = sum(matches[a, b].values())
    if count >= 66:
        overlapping[a].add(b)
        overlapping[b].add(a)

# Start with scanner 0
scanner_rotations: Dict[ScannerId, np.ndarray] = {0: rotation_matricies[3]}
scanner_positions: Dict[ScannerId, V3] = {0: (0, 0, 0)}
todo: Set[ScannerId] = set([0])
# While there are scanners we can resolve relative to scanner 0
while todo:
    this = todo.pop()
    # For each scanner that might overlap
    for other in overlapping[this]:
        if other not in scanner_positions:
            todo.add(other)
            pair = (min(this, other), max(this, other))
            # Pick a delta
            for delta in matches[pair]:
                # From the perspective of this scanner, find the two beacons that delta came from
                this_a, this_b = delta_map[this][delta]
                # Calculate the positions relative to scanner 0
                this_a = rotate(this_a, scanner_rotations[this])
                this_a = add(this_a, scanner_positions[this])
                this_b = rotate(this_b, scanner_rotations[this])
                this_b = add(this_b, scanner_positions[this])
                # Get the non-normalized delta in this scanner's reference frame
                this_diff = diff(this_a, this_b)
                # From the perspective of the other scanner, get the two beacons for that delta
                other_a, other_b = delta_map[other][delta]
                # Get the non-normalized delta and find a rotation of it that matches the one from this delta
                other_diff = diff(other_a, other_b)
                rot_index = find_rot(this_diff, other_diff)
                if rot_index is not None:
                    # If we found a rotation, save the rotation and position of the other scanner
                    scanner_rotations[other] = rotation_matricies[rot_index]
                    scanner_positions[other] = diff(
                        this_a, rotate(other_a, scanner_rotations[other])
                    )
                    break
                # If we didn't find a rotation, try again with the points swapped
                other_diff = diff(other_b, other_a)
                rot_index = find_rot(this_diff, other_diff)
                if rot_index is not None:
                    scanner_rotations[other] = rotation_matricies[rot_index]
                    scanner_positions[other] = diff(
                        this_a, rotate(other_b, scanner_rotations[other])
                    )
                    break

# For every beacon in every scanner, store the beacon positions relative to scanner 0
all_beacons: Set[V3] = set()
for scanner, beacons in scanners.items():
    for b in beacons:
        all_beacons.add(
            add(scanner_positions[scanner], rotate(b, scanner_rotations[scanner]))
        )
print(len(all_beacons))
