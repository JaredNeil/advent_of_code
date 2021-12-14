from collections import defaultdict
from itertools import repeat

from parse import load_lines, s

(lines,) = load_lines(repeat(s))

edges = defaultdict(set)
for l in lines:
    f, t = l.split('-')
    edges[f].add(t)
    edges[t].add(f)

def find_paths(pos, path, small):
    if pos == "end":
        return 1
    paths = 0
    for n in edges[pos]:
        if n == "start":
            pass
        elif n == n.lower() and n in path:
            if small:
                paths += find_paths(n, path + [n], False)
        else:
            paths += find_paths(n, path + [n], small)
    return paths


r = find_paths("start", ["start"], True)
print(r)
