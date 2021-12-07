from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product, chain

from util import load_lines, transpose, window_of

lines = list(load_lines())

nums=list(map(int, lines[0].split(',')))

boards = []

for i in range(2, len(lines)-2, 6):
    board = [list(map(int, l.split())) for l in lines[i:i+5]]
    wins = [set(l) for l in board + list(transpose(board))]
    boards.append({"wins": wins,"won": False, "all": set(chain.from_iterable(board))})


for n in nums:
    for board in boards:
        board["all"].discard(n)
        for win in board["wins"]:
            win.discard(n)
            if not win:
                board["won"] = True
                if len(boards) == 1:
                    print(sum(board["all"]) * n)
                    exit(0)
    boards = list(filter(lambda b: b["won"] == False, boards))


