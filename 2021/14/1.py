from collections import Counter
from itertools import repeat, chain

from parse import load_lines, s
from util import window_of

(template, insertions) = load_lines(s, repeat(s))

subs = {}
for sub in insertions:
    l, r = sub.split(" -> ")
    subs[tuple(l)] = r


poly = list(template)
for _ in range(10):
    chains = []
    for pair in window_of(2, poly + [None]):
        if pair in subs:
            chains.append([pair[0], subs[pair]])
        else:
            chains.append([pair[0]])
    poly = list(chain.from_iterable(chains))

most, *_, least = Counter(poly).most_common()

print(most[1] - least[1])

