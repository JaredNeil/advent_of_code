from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product, repeat

from parse import line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of


@lru_cache(None)
def digit(w, z, z_div, x_add, y_add):
    x = z
    x %= 26
    z //= z_div
    x += x_add
    if x != w:
        z *= 26
        z += (w + y_add)
    return z

parameters = {
    0:  ( 1,  15, 15),
    1:  ( 1,  15, 10),
    2:  ( 1,  12,  2),
    3:  ( 1,  13, 16),
    4:  (26, -12, 12),
    5:  ( 1,  10, 11),
    6:  (26, - 9,  5),
    7:  ( 1,  14, 16),
    8:  ( 1,  13,  6),
    9:  (26, -14, 15),
    10: (26, -11,  3),
    11: (26, - 2, 12),
    12: (26, -16, 10),
    13: (26, -14, 13),
}
possible = defaultdict(set)
possible[-1].add(0)

for n in range(14):
    for z in possible[n-1]:
        for w in range(1, 10):
            possible[n].add(digit(w, z, *parameters[n]))
    del possible[n-1]
    pp(n, len(possible[n]), min(possible[n]), max(possible[n]))
print(0 in possible[13])
exit(0)

valid = defaultdict(dict)
valid[14] = {0: True}
for i in range(13, -1, -1):
    z = 0
    while z < 1000000:
        for w in range(1,10):
            d = digit(w, z, *parameters[i])
            if d in valid[i+1]:
                # print(i, w, z, d)
                valid[i][z] = d
            d = digit(w, -z, *parameters[i])
            if d in valid[i+1]:
                # print(i, w, -z, d)
                valid[i][-z] = d
        z += 1
    # print(i, "up to", z)
pp(valid[0])
pp(valid[1])
pp(valid[2])
pp(valid[3])
# try:
#     for n in product([9,8,7,6,5,4,3,2,1], repeat=14):
#         if n[7] == 9 and n[8] == 9 and n[9] == 9 and n[10] == 9 and n[11] == 9 and n[12] == 9 and n[13] == 9:
#             pp(n)
#         z = digit(n[0], 0, 1, 15, 15)
#         z = digit(n[1], z, 1, 15, 10)
#         z = digit(n[2], z, 1, 12, 2)
#         z = digit(n[3], z, 1, 13, 16)
#         z = digit(n[4], z, 26, -12, 12)
#         z = digit(n[5], z, 1, 10, 11)
#         z = digit(n[6], z, 26, -9, 5)
#         z = digit(n[7], z, 1, 14, 16)
#         z = digit(n[8], z, 1, 13, 6)
#         z = digit(n[9], z, 26, -14, 15)
#         z = digit(n[10], z, 26, -11, 3)
#         z = digit(n[11], z, 26, -2, 12)
#         z = digit(n[12], z, 26, -16, 10)
#         z = digit(n[13], z, 26, -14, 13)
#         if z == 0:
#             print("Answer", n)
#             break
# except:
#     print(digit.cache_info())
