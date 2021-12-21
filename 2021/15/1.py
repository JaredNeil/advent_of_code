from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat
from heapq import heappush, heappop
from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, n4, pp, transpose, window_of

(lines,) = load_lines(repeat(s))

grid = make_grid(lines)

risk = 0
goal = max(grid)
visited = set()
edge = [(0, (0, 0))]
while True:
    risk, pos = heappop(edge)
    # pp(risk, pos)
    if pos == goal:
        print(risk)
        break
    visited.add(pos)
    for npos in n4(*pos):
        if npos in grid and npos not in visited:
            heappush(edge, (risk + grid[npos], npos))
