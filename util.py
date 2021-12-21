import sys
from collections import defaultdict
from itertools import islice, tee
from pprint import PrettyPrinter


def window_of(size, iter):
    return zip(*[islice(it, i, None) for i, it in enumerate(tee(iter, size))])


def transpose(grid):
    return list(zip(*grid))


def mapint(iter):
    return list(map(int, iter))


def chunks_of(size, l):
    return [l[i : i + size] for i in range(0, len(l), size)]


def triangular(n):
    return n * (n + 1) // 2

_pp = PrettyPrinter(
    indent=2,
    width=120,
    stream=sys.stderr,
    compact=True,
)
def pp(*args):
    if len(args) == 1:
        _pp.pprint(args[0])
    else:
        _pp.pprint(args)


def mul(iter):
    result = 1
    for n in iter:
        result *= n
    return result


DELTAS4 = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
]


def n4(x, y):
    result = []
    for dx, dy in DELTAS4:
        result.append((x + dx, y + dy))
    return result


DELTAS8 = DELTAS4 + [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def n8(x, y):
    result = []
    for dx, dy in DELTAS8:
        result.append((x + dx, y + dy))
    return result


def make_grid(lines, default=None):
    if default is None:
        grid = {}
    else:
        grid = defaultdict(default)
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            grid[x, y] = c
    return grid


def extants(grid, filter = lambda x: True):
    xs = [x for x, y in grid if filter(((x,y), grid[x, y]))]
    ys = [y for x, y in grid if filter(((x,y), grid[x, y]))]
    return ((min(xs), max(xs)), (min(ys), max(ys)))


def display(grid, default=" ", filter=lambda x: True):
    ((min_x, max_x), (min_y, max_y)) = extants(grid, filter)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid.get((x, y), default), end="")
        print("")
