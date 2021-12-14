from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import Point, cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, extants, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(s))

points = []
folds = []
for l in lines:
    if l.startswith("fold"):
        folds.append(l.split()[2])
    elif l != "":
        points.append(Point(l))


for f in folds[:1]:
    d, v = f.split("=")
    if d == "x":
        x = int(v)
        for p in points:
            if p.x > x:
                nx = x - (p.x - x)
                p.x = nx
    else:
        y = int(v)
        for p in points:
            if p.y > y:
                ny = y - (p.y - y)
                p.y = ny

grid = defaultdict(lambda: ' ')
for p in points:
    grid[p.x, p.y] = "#"
print(len(grid))