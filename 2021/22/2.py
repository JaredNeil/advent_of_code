from dataclasses import dataclass
from itertools import repeat

from parse import load_lines, s
from util import mapint


@dataclass
class Region:
    value: int
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int


def intersection(a: Region, b: Region) -> Region:
    if (
        a.min_x <= b.max_x
        and b.min_x <= a.max_x
        and a.min_y <= b.max_y
        and b.min_y <= a.max_y
        and a.min_z <= b.max_z
        and b.min_z <= a.max_z
    ):
        return Region(
            -b.value,
            max(a.min_x, b.min_x),
            min(a.max_x, b.max_x),
            max(a.min_y, b.min_y),
            min(a.max_y, b.max_y),
            max(a.min_z, b.min_z),
            min(a.max_z, b.max_z),
        )
    else:
        return None


def val(r: Region) -> int:
    return (
        r.value
        * (1 + r.max_x - r.min_x)
        * (1 + r.max_y - r.min_y)
        * (1 + r.max_z - r.min_z)
    )


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

regions = []
for c, (xs, ys, zs) in commands:
    this = Region(int(c), *xs, *ys, *zs)
    overlap = False
    for other in regions.copy():
        i = intersection(this, other)
        if i:
            regions.append(i)
    if this.value == 1:
        regions.append(this)

print(sum(val(r) for r in regions))
