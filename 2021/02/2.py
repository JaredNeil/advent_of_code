from itertools import repeat
from util import load_lines, wls

(lines,) = load_lines(repeat(wls))
commands = map(lambda x: (x[0], int(x[1])), lines)
pos = 0
depth = 0
aim = 0
for c, x in commands:
    if c == "forward":
        pos += x
        depth += x*aim
    elif c == "down":
        aim += x
    elif c == "up":
        aim -= x

print(pos*depth)