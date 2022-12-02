from itertools import repeat
from parse import load_lines, s

(lines,) = load_lines(repeat(s))

scores = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    },
}

score = 0
for l in lines:
    them, me = l.split()
    score += scores[them][me]

print(score)