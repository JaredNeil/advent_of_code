from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product

from util import load_lines, transpose, window_of

lines = list(load_lines(lambda start, _, end: (tuple(map(int, start.split(','))), tuple(map(int, end.split(','))))))

grid = defaultdict(int)

for (sx, sy), (ex, ey) in lines:
    if sx == ex:
        for y in range(min(sy, ey), max(sy, ey)+1):
            grid[sx,y] += 1
    elif sy == ey:
        for x in range(min(sx, ex), max(sx, ex)+1):
            grid[x,sy] += 1
    else:
        dx = 1 if sx < ex else -1
        dy = 1 if sy < ey else -1
        for x, y in zip(range(sx, ex+dx, dx), range(sy, ey+dy, dy)):
            grid[x,y] += 1

for y in range(9):
    for x in range(9):
        print(grid[x,y], end='')
    print('')
print(len(list(filter(lambda n: n >1, grid.values()))))
