from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, display, extants, make_grid, mul, n8, pp, transpose, window_of

(subs,  image) = load_lines(s, repeat(s))

grid = make_grid(image, lambda: '.')
lookup = {
    ".": "0",
    "#": "1",
}

def enhance(grid, fill= "0"):
    result = defaultdict(lambda: '.')
    ((min_x, max_x), (min_y, max_y)) = extants(grid)
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            bits = []
            for pos in sorted(n8(x, y) + [(x, y)], key=lambda p: (p[1],p[0])):
                if pos in grid:
                    bits.append(lookup[grid[pos]])
                else:
                    bits.append(fill)
            n = int(''.join(bits), 2)
            result[x, y] = subs[n]
    return result

for i in range(50):
    grid = enhance(grid, str(i%2))

counts = Counter(grid.values())
print(counts["#"])