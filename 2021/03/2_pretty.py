from collections import defaultdict, Counter
from functools import lru_cache
from operator import itemgetter
from itertools import combinations, permutations, product

from util import transpose, window_of, load_lines

lines = load_lines()
# Reverse sort the list so "1" shows up first from `.most_common` in the event of a tie
ox = list(sorted(lines, reverse=True))
co2 = ox.copy()
for col in range(len(ox[0])):
    ox_common = Counter(map(itemgetter(col), ox)).most_common()[0]
    ox = list(filter(lambda l: l[col] == ox_common[0], ox))
    co2_common = Counter(map(itemgetter(col), co2)).most_common()[-1]
    co2 = list(filter(lambda l: l[col] == co2_common[0], co2))
print(int(ox[0], 2) * int(co2[0], 2))
