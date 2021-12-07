from collections import Counter
from util import transpose, load_lines

lines = list(load_lines(str))

gamma = ""
epsilon = ""
for c in transpose(lines):
    common = Counter(c).most_common()
    gamma += common[0][0]
    epsilon += common[-1][0]
print(int(gamma, 2) * int(epsilon, 2))
