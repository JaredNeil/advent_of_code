from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from os import EX_NOPERM

from util import window_of, load_lines

lines = list(load_lines(str))

ox = list(lines)
for pos in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in ox:
        if line[pos] == "0":
            zeros += 1
        elif line[pos] == "1":
            ones += 1
    if ones >= zeros:
        ox = list(filter(lambda x: x[pos] == "1", ox))
    else:
        ox = list(filter(lambda x: x[pos] == "0", ox))
    if len(ox) == 1:
        ox_r = int(ox[0], 2)
        break

co2 = list(lines)
for pos in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in co2:
        if line[pos] == "0":
            zeros += 1
        elif line[pos] == "1":
            ones += 1
    if ones >= zeros:
        co2 = list(filter(lambda x: x[pos] == "0", co2))
    else:
        co2 = list(filter(lambda x: x[pos] == "1", co2))
    if len(co2) == 1:
        co2_r = int(co2[0], 2)
        break

print(ox_r, co2_r)
print(ox_r * co2_r)
