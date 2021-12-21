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
print(message)


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

    p = Packet(num(3), num(3), None, [], None)
    if p.type == 4:
        more = True
        nibs = []
        while more:
            more = get(1) == "1"
            nibs.append(get(4))
        p.value = int("".join(nibs), 2)
    else:
        if get(1) == "0":
            length = num(15)
            end = read + length
            while read < end:
                sub = parse_packet(stream)
                p.children.append(sub)
                read += sub.length
        else:
            packets = num(11)
            for _ in range(packets):
                sub = parse_packet(stream)
                p.children.append(sub)
                read += sub.length
    p.length = read
    return p


packet = parse_packet(chain(message))

def sum_versions(packet: Packet):
    return packet.version + sum(map(sum_versions, packet.children))

print(sum_versions(packet))