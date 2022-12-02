import sys

print(
    max(sum(int(i) for i in l.split()) for l in open(sys.argv[1]).read().split("\n\n"))
)
