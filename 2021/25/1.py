from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, display, extants, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(s))

grid = make_grid(lines)
(_, X), (_, Y) = extants(grid)
X += 1
Y += 1
empty = set(pos for pos in grid if grid[pos] == '.')
moved = True
step = 0
while moved:
    moved = False
    move = {}
    for pos in empty:
        x, y=pos
        left = (x-1)%X, y
        if grid[left] == '>':
            move[pos] = left
    if move:
        moved = True
    for t, f in move.items():
        grid[t] = '>'
        empty.remove(t)
        grid[f] = '.'
        empty.add(f)

    move = {}
    for pos in empty:
        x, y=pos
        up = x, (y-1)%Y
        if grid[up] == 'v':
            move[pos] = up
    if move:
        moved = True
    for t, f in move.items():
        grid[t] = 'v'
        empty.remove(t)
        grid[f] = '.'
        empty.add(f)
    step += 1
    print(step)
    display(grid)

