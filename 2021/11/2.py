from itertools import repeat

from parse import load_lines, s
from util import make_grid, n8

(lines,) = load_lines(repeat(s))
grid = make_grid(lines)
step = 0
while True:
    step += 1
    flash = set()
    flashed = set()
    for pos in grid:
        grid[pos] += 1
        if grid[pos] > 9:
            flash.add(pos)
    while flash:
        f = flash.pop()
        flashed.add(f)
        for npos in n8(*f):
            if npos in grid and npos not in flashed:
                grid[npos] += 1
                if grid[npos] > 9:
                    flash.add(npos)
    for pos in flashed:
        grid[pos] = 0
    if len(flashed) == len(grid):
        break

print(step)