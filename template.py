from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product

from util import load_lines, transpose, window_of, cli

(nums,) = load_lines(cli)
