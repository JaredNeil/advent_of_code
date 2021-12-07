from itertools import repeat

from util import i, window_of, load_lines

(nums,) = load_lines(repeat(i))
sums = map(sum, window_of(3, nums))
print(sum(a < b for a, b in window_of(2, sums)))
