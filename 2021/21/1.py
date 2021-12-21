from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, islice, permutations, product, repeat, cycle

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(s))

p0 = int(lines[0].split()[4])-1
p1 = int(lines[1].split()[4])-1
positions = [p0, p1]
scores = [0, 0]
die = cycle(range(1, 101))
rolls = 0
turn = 0
while max(scores) < 1000:
    move = sum(islice(die, 3))
    rolls += 3
    positions[turn] = (positions[turn] + move) % 10
    scores[turn] += positions[turn] + 1
    turn = (turn + 1) % 2

print(min(scores)*rolls)
