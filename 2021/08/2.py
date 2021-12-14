from collections import Counter, defaultdict
from itertools import repeat

from util import load_lines, wls

(notes,) = load_lines(repeat(wls))

digits = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}
count_map = {
    4: "e",
    6: "b",
    9: "f",
}
full = "abcdefg"
total = 0
for note in notes:
    mapping = {}
    patterns = ["".join(sorted(d)) for d in note[:10]]
    lengths = defaultdict(list)
    counts = Counter()
    for p in patterns:
        counts.update(p)
        lengths[len(p)].append(p)
    for c, count in counts.items():
        if count in count_map:
            mapping[c] = count_map[count]  # "bef"

    for c in lengths[2][0]:
        if c not in mapping:
            mapping[c] = "c"
    for c in lengths[3][0]:
        if c not in mapping:
            mapping[c] = "a"
    for c in lengths[4][0]:
        if c not in mapping:
            mapping[c] = "d"
    for c in full:
        if c not in mapping:
            mapping[c] = "g"
    values = note[-4:]
    num = ""
    for v in values:
        num += digits["".join(sorted(mapping[c] for c in v))]
    total += int(num)
print(total)
