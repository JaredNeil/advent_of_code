from collections import Counter, defaultdict, deque
from functools import lru_cache
from heapq import heappop, heappush
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import extants, make_grid, n4, pp

(lines,) = load_lines(repeat(s))

grid = make_grid(lines)

((_, X), (_, Y)) = extants(grid)
pp(extants(grid))
for pos in list(grid):
    px, py = pos
    for y in range(5):
        for x in range(5):
            npos = ((X + 1) * x + px, (Y + 1) * y + py)
            grid[npos] = 1 + (grid[pos] + y + x - 1) % 9
pp(extants(grid))
risk = 0
goal = max(grid)
seen = set([(0, 0)])
edge = [(0, (0, 0))]
while edge:
    risk, pos = heappop(edge)
    pp(risk, pos)
    if pos == goal:
        print(risk)
        break
    for npos in n4(*pos):
        if npos in grid and npos not in seen:
            seen.add(npos)
            heappush(edge, (risk + grid[npos], npos))
