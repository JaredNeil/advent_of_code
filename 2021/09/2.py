from collections import Counter
from itertools import repeat

from util import load_lines, make_grid, mul, n4, s

(lines,) = load_lines(repeat(s))
grid = make_grid(lines, lambda: 10)
lows = set()
for pos in list(grid):
    if not any(grid[pos] >= grid[npos] for npos in n4(*pos)):
        lows.add(pos)

sizes = Counter()
for low in lows:
    basin = set()
    edge = set([low])
    while edge:
        pos = edge.pop()
        basin.add(pos)
        x, y = pos
        for npos in n4(x, y):
            if npos not in basin and grid[npos] < 9:
                edge.add(npos)
    sizes[low] = len(basin)

largest = sizes.most_common(3)
print(mul(l[1] for l in largest))
