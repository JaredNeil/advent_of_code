from functools import lru_cache
from itertools import product, repeat

from parse import load_lines, s


@lru_cache(None)
def wins(p0, p1, s0, s1):
    if s1 >= 21:
        return [0, 1]
    else:
        outcomes = [0, 0]
        for rolls in product(range(1, 4), repeat=3):
            move = sum(rolls)
            new_pos = (p0 + move) % 10
            new_score = s0 + new_pos + 1
            w1, w0 = wins(p1, new_pos, s1, new_score)
            outcomes[0] += w0
            outcomes[1] += w1
        return outcomes


(lines,) = load_lines(repeat(s))
p0 = int(lines[0].split()[4]) - 1
p1 = int(lines[1].split()[4]) - 1
print(max(wins(p0, p1, 0, 0)))

for p0 in range(10):
    for p1 in range(10):
        print(p0, p1, wins(p0, p1, 0, 0))
print(wins.cache_info())
