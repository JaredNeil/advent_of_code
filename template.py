from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(lines,) = load_lines(repeat(s))
