from util import load_lines, cli

(nums,) = load_lines(cli)

print(
    min(
        sum(
            abs(pos-x) for x in nums
        ) for pos in range(min(nums), max(nums)+1)
    )
)