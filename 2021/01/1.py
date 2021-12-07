from itertools import repeat

from util import window_of, load_lines, i

(nums,) = load_lines(repeat(i))
print(sum(a < b for a, b in window_of(2, nums)))
