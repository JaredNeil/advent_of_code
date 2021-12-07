import sys
from collections import namedtuple
from collections.abc import Iterable
from dataclasses import dataclass
from itertools import chain, islice, starmap, tee

import nifty_nesting as nest
from nifty_nesting.nifty_nesting import is_scalar


def load_lines(*structure, keep_empty=False):
    # with open(sys.argv[1]) as f:
    with open(sys.argv[1]) as f:
        stripped = (l.strip() for l in f)
        iter = filter(lambda x: keep_empty or x, stripped)
        return parse(structure, iter)


def parse(structure, iter):
    parsed = []
    try:
        for val in nest.flatten(structure):
            if isinstance(val, Iterable):
                part = []
                try:
                    for p in val:
                        if is_scalar(p):
                            part.append(p(iter))
                        else:
                            part.append(parse(p, iter))
                except StopIteration:
                    pass
                finally:
                    parsed.append(part)
            else:
                parsed.append(val(iter))
    except StopIteration:
        pass
    # print("s", structure)
    # print("p", parsed)
    return nest.pack_list_into(structure, parsed)


def _l(it, sep, f):
    return list(map(f, next(it).split(sep)))


def i(it):
    return int(next(it))


def s(it):
    return str(next(it))


def l(sep, f):
    return lambda it: _l(it, sep, f)


cli = l(",", int)
cls = l(",", str)
wli = l(None, int)
wls = l(None, str)


def grid(n, sep=None, f=int):
    return lambda it: [_l(it, sep, f) for _ in range(n)]

class Point:
    x: int
    y: int
    def __init__(self, s):
        self.x, self.y = map(int, s.split(","))

class Line:
    start: Point
    end: Point
    def __init__(self, s):
        self.start, self.end = map(Point, s.split(" -> "))

def line(iter):
    return Line(next(iter))

def window_of(size, iter):
    return zip(*[islice(it, i, None) for i, it in enumerate(tee(iter, size))])


def transpose(grid):
    return list(zip(*grid))


def mapint(iter):
    return list(map(int, iter))


def chunks_of(size, l):
    return [l[i : i + size] for i in range(0, len(l), size)]

def triangular(n):
    return n * (n+1) // 2