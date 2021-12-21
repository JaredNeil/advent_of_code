from collections import Counter
from functools import lru_cache
from itertools import repeat

from parse import load_lines, s
from util import window_of, pp

(template, insertions) = load_lines(s, repeat(lambda it: next(it).split(" -> ")))

rules = {tuple(pair): insert for pair, insert in insertions}
counts = Counter(window_of(2, template + " "))
for _ in range(40):
    new_counts = Counter()
    for match, count in counts.items():
        if match in rules:
            new_counts[match[0], rules[match]] += count
            new_counts[rules[match], match[1]] += count
        else:
            new_counts[match] += count
    counts = new_counts

result = Counter()
for k, v in counts.items():
    result[k[0]] += v
mx = max(result.values())
mn = min(result.values())
print(mx - mn)