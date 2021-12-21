from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product, repeat, chain
from typing import List

from parse import cli, cls, i, line, load_lines, point, s, table, wli, wls
from util import chunks_of, make_grid, mul, pp, transpose, window_of

(hex_message,) = load_lines(s)

strings = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

message = "".join(strings[c] for c in hex_message)


@dataclass
class Packet:
    version: int
    type: int
    value: int
    children: List[Packet]
    length: int


def parse_packet(stream):
    read = 0

    def get(n):
        nonlocal read
        read += n
        return "".join(next(stream) for _ in range(n))

    def num(n):
        return int(get(n), 2)

    def next_bool():
        return get(1) == "1"

    p = Packet(num(3), num(3), None, [], None)
    if p.type == 4:
        more = True
        nibs = []
        while more:
            more = next_bool()
            nibs.append(get(4))
        p.value = int("".join(nibs), 2)
    else:
        if next_bool():
            packets = num(11)
            for _ in range(packets):
                sub = parse_packet(stream)
                p.children.append(sub)
                read += sub.length
        else:
            length = num(15)
            end = read + length
            while read < end:
                sub = parse_packet(stream)
                p.children.append(sub)
                read += sub.length
        vals = [sub.value for sub in p.children]
        if p.type == 0:
            p.value = sum(vals)
        elif p.type == 1:
            p.value = mul(vals)
        elif p.type == 2:
            p.value = min(vals)
        elif p.type == 3:
            p.value = max(vals)
        elif p.type == 5:
            p.value = 1 if vals[0] > vals[1] else 0
        elif p.type == 6:
            p.value = 1 if vals[0] < vals[1] else 0
        elif p.type == 7:
            p.value = 1 if vals[0] == vals[1] else 0
    p.length = read
    return p


packet = parse_packet(chain(message))
print(packet.value)