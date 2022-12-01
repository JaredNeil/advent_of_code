from collections import defaultdict
from itertools import repeat

from parse import load_lines, s
from util import mapint


def intersects_area(low, high):
    return low <= 50 and high >= -50


(lines,) = load_lines(repeat(s))
commands = []
for l in lines:
    c, coords = l.split()
    (
        xs,
        ys,
        zs,
    ) = map(lambda s: tuple(mapint(s[2:].split(".."))), coords.split(","))
    commands.append((c == "on", (xs, ys, zs)))

reactor = defaultdict(lambda: False)

for c, coords in commands:
    overlap = all(intersects_area(low, high) for low, high in coords)
    if overlap:
        (minx, maxx), (miny, maxy), (minz, maxz) = coords
        for x in range(max(-50, minx), min(50, maxx) + 1):
            for y in range(max(-50, miny), min(50, maxy) + 1):
                for z in range(max(-50, minz), min(50, maxz) + 1):
                    reactor[x, y, z] = c

print(sum(reactor.values()))
