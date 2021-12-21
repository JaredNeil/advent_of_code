import os
from collections import Counter
from itertools import repeat
from time import sleep

from parse import load_lines, s
from util import display, extants, make_grid, n8

(subs, image) = load_lines(s, repeat(s))

grid = make_grid(image, lambda: ".")
lookup = {
    ".": "0",
    "#": "1",
}


def enhance(grid):
    result = {}
    ((min_x, max_x), (min_y, max_y)) = extants(grid)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            bits = []
            for pos in sorted(n8(x, y) + [(x, y)], key=lambda p: (p[1], p[0])):
                if pos in grid:
                    bits.append(lookup[grid[pos]])
                else:
                    bits.append("0")
            n = int("".join(bits), 2)
            if subs[n] == "#":
                result[x, y] = subs[n]
    return result


while True:
    grid = enhance(grid)
    os.system("clear")
    display(grid, filter=lambda kv: kv[1] == "#")
    sleep(0.05)

