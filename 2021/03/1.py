from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from os import EX_NOPERM

from util import transpose, window_of, load_lines

lines = list(load_lines(str))

gamma = []
epsilon = []
for pos in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[pos] == '0':
            zeros += 1
        elif line[pos] == '1':
            ones += 1

    if zeros > ones:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))

x = transpose(lines)
print(x[0])