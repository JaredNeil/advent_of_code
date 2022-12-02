import sys

print(
    sum(
        {
            "A": {
                "X": 1 + 3,
                "Y": 2 + 6,
                "Z": 3 + 0,
            },
            "B": {
                "X": 1 + 0,
                "Y": 2 + 3,
                "Z": 3 + 6,
            },
            "C": {
                "X": 1 + 6,
                "Y": 2 + 0,
                "Z": 3 + 3,
            },
        }[line[0]][line[2]]
        for line in open(sys.argv[1])
    )
)
