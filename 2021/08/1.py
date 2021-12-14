from itertools import repeat

from util import load_lines, wls

(notes,) = load_lines(repeat(wls))

unique_patterns = set([2, 3, 4, 7])
total = 0
for note in notes:
    patterns = note[:10]
    values = note[-4:]
    for v in values:
        if len(v) in unique_patterns:
            total += 1
print(total)
