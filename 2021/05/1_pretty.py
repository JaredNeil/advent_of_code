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
for x in range(9):
    for y in range(9):
        print(grid[x,y], end='')
    print('')
# print(grid.values())
print(len(list(filter(lambda n: n >1, grid.values()))))
