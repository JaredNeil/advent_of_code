from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(s))

p = 0
for l in lines:
    n = len(l)//2
    both = set(l[:n]) & set(l[n:])
    for i in both:
        if "a" <= i <= "z":
            p += ord(i) - ord("a") + 1
        elif "A" <= i <= "Z":
            p += ord(i) - ord("A") + 27

print(p)