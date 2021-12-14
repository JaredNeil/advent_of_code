from itertools import  repeat

from util import load_lines, make_grid, n4, s

(lines,) = load_lines(repeat(s))
grid = make_grid(lines, lambda: 10)
lows = set()
for pos in list(grid):
    if not any(grid[pos] >= grid[npos] for npos in n4(*pos)):
        lows.add(pos)

print(sum(1+grid[pos] for pos in lows))
