from collections import Counter
from functools import lru_cache
from itertools import repeat

from parse import load_lines, s
from util import window_of

(template, insertions) = load_lines(s, repeat(lambda it: next(it).split(" -> ")))

subs = {tuple(pair): insert for pair, insert in insertions}

@lru_cache(None)
def expand(l, r, height):
    pair = (l, r)
    if height > 0 and pair in subs:
        return expand(l, subs[pair], height - 1) + expand(subs[pair], r, height - 1)
    else:
        return Counter(l)

counts = sum((expand(l, r, 40) for l, r in window_of(2, template + " ")), Counter())
(_, most), *_, (_, least) = counts.most_common()
print(most - least)
