from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(groups,) = load_lines(repeat((s, s, s)))

p = 0
for a, b, c in groups:
    common = set(a) & set(b) & set(c)
    for i in common:
        if "a" <= i <= "z":
            p += ord(i) - ord("a") + 1
        elif "A" <= i <= "Z":
            p += ord(i) - ord("A") + 27

print(p)