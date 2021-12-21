from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, display, make_grid, mapint, mul, pp, transpose, window_of

(parts,) = load_lines(wls)

minx, maxx = mapint(parts[2][2:-1].split(".."))
miny, maxy = mapint(parts[3][2:].split(".."))

def sim(dx, dy):
    x, y = 0, 0
    height = 0
    while y >= miny:
        x += dx
        y += dy
        height = max(height, y)
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        if minx <= x <= maxx and miny <= y <= maxy:
            return height

hits = set()
for dy in range(miny-2, -miny+2):
    for dx in range(maxx+2):
        height = sim(dx, dy)
        if height is not None:
            hits.add((dx, dy))
print(len(hits))
