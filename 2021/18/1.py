from __future__ import annotations

from copy import deepcopy
from itertools import repeat
from typing import List

import nifty_nesting as nest
from parse import load_lines, s
from util import pp


def add(l, r):
    return [l, r]


def find_explode(num, path=[]):
    if isinstance(num, list):
        if isinstance(num[0], int) and isinstance(num[1], int) and len(path) >= 4:
            return path, 0
        else:
            found_path, l_size = find_explode(num[0], path + [0])
            if found_path is not None:
                return found_path, l_size
            found_path, r_size = find_explode(num[1], path + [1])
            if found_path is not None:
                return found_path, l_size + r_size
            return None, l_size + r_size
    else:
        return None, 1


def explode(num, path, index):
    structure = deepcopy(num)
    cur = structure
    for side in path[:-1]:
        cur = cur[side]
    pp("exploding", cur[path[-1]])
    cur[path[-1]] = None
    flat = nest.flatten(num)
    ld = index - 1
    if ld >= 0:
        flat[ld] += flat[index]
    rd = index + 2
    if rd < len(flat):
        flat[rd] += flat[index + 1]
    del flat[index]
    flat[index] = 0
    return nest.pack_list_into(structure, flat)


def find_split(num, path=[]):
    if isinstance(num, int):
        if num > 9:
            return path, 0
        else:
            return None, 1
    else:
        found_path, l_size = find_split(num[0], path + [0])
        if found_path is not None:
            return found_path, l_size
        found_path, r_size = find_split(num[1], path + [1])
        if found_path is not None:
            return found_path, l_size + r_size
        return None, l_size + r_size


def split(num, path, index):
    structure = deepcopy(num)
    cur = structure
    for side in path[:-1]:
        cur = cur[side]
    pp("splitting", cur[path[-1]])
    cur[path[-1]] = [None, None]
    flat: List = nest.flatten(num)
    old = flat[index]
    flat[index] = old // 2
    flat.insert(index + 1, (old + 1) // 2)
    return nest.pack_list_into(structure, flat)


def mag(num):
    if isinstance(num, int):
        return num
    else:
        return 3 * mag(num[0]) + 2 * mag(num[1])


def reduce(num):
    cur = deepcopy(num)
    while True:
        pp(cur)
        path, index = find_explode(cur)
        if path is not None:
            cur = explode(cur, path, index)
            continue
        path, index = find_split(cur)
        if path is not None:
            cur = split(cur, path, index)
            continue
        break
    return cur


(lines,) = load_lines(repeat(s))
nums = [eval(line) for line in lines]

num = nums[0]
for n in nums[1:]:
    num = add(num, n)
    num = reduce(num)

pp(mag(num))
