from collections import  defaultdict

from util import load_lines, cli

(ages,) = load_lines(cli)
fish = defaultdict(int)
for n in ages:
    fish[n] += 1
for i in range(256):
    n_fish = defaultdict(int)
    for age, count in fish.items():
        if age == 0:
            n_fish[6] += count
            n_fish[8] += count
        else:
            n_fish[age-1] += count
    fish = n_fish
print(sum(fish.values()))
