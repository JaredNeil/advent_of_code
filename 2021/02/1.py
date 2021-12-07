from itertools import repeat

from util import load_lines, wls

(lines,) = load_lines(repeat(wls))
commands = map(lambda x: (x[0], int(x[1])), lines)

x = 0
depth = 0
for d, dist in commands:
    if d == "forward":
        x += dist
    elif d == "down":
        depth += dist
    elif d == "up":
        depth -= dist
    print(x,depth)

print(x*depth)