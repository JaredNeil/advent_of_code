from itertools import repeat
from parse import load_lines, s

(lines,) = load_lines(repeat(s))

score = 0
for l in lines:
    them, me = l.split()
    if them == "A":
        if me == "X":
            score += 1 + 3
        elif me == "Y":
            score += 2 + 6
        elif me == "Z":
            score += 3 + 0
    elif them == "B":
        if me == "X":
            score += 1 + 0
        elif me == "Y":
            score += 2 + 3
        elif me == "Z":
            score += 3 + 6
    elif them == "C":
        if me == "X":
            score += 1 + 6
        elif me == "Y":
            score += 2 + 0
        elif me == "Z":
            score += 3 + 3

print(score)