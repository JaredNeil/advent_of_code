import sys
from itertools import islice

print(
    sum(
        islice(
            sorted(
                (
                    sum(int(i) for i in l.split())
                    for l in open(sys.argv[1]).read().split("\n\n")
                ),
                reverse=True,
            ),
            3,
        )
    )
)
