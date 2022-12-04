from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, l, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(l(r"[-,]", int)))

count = 0
for s0, e0, s1, e1 in lines:
    if e0 >= s1 and e1 >= s0:
        count += 1
    elif e1 >= s0 and e0 >= s1:
        count += 1

print(count)
