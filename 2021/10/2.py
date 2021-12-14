from itertools import repeat
from statistics import median

from util import load_lines, s

(lines,) = load_lines(repeat(s))

brackets = {
    "<": ">",
    "(": ")",
    "[": "]",
    "{": "}",
}
scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

all_scores = []
for line in lines:
    stack = []
    score = 0
    for c in line:
        if c in brackets:
            stack.append(brackets[c])
        elif c in scores:
            if stack.pop() != c:
                break
    else:
        for c in reversed(stack):
            score *= 5
            score += scores[c]
        all_scores.append(score)

print(median(all_scores))
