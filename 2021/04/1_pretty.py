from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product, chain, repeat

from util import load_lines, transpose, window_of, cli, grid

called, boards = list(load_lines(cli, repeat(grid(5, f=int))))
print(called)
print(boards)

exit()
nums=list(map(int, lines[0].split(',')))

boards = []

for i in range(2, len(lines)-2, 6):
    board = [list(map(int, l.split())) for l in lines[i:i+5]]
    wins = [set(l) for l in board + list(transpose(board))]
    boards.append({"wins": wins, "all": set(chain.from_iterable(board))})


for n in nums:
    for board in boards:
        board["all"].discard(n)
        for win in board["wins"]:
            win.discard(n)
            if not win:
                print(sum(board["all"])*n)
                exit(0)


