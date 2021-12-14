from itertools import repeat

from util import load_lines, s

(lines,) = load_lines(repeat(s))

brackets = {
    "<": ">",
    "(": ")",
    "[": "]",
    "{": "}",
}
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

total = 0
for line in lines:
    stack = []
    for c in line:
        if c in brackets:
            stack.append(brackets[c])
        elif c in scores:
            if stack.pop() != c:
                total += scores[c]
                break
print(total)