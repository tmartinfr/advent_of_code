from collections import defaultdict


fish = defaultdict(int)
for n in open('06a_input').readline().strip().split(','):
    fish[int(n)] += 1

day = 0
while day < 256:
    day += 1
    new_fish = defaultdict(int)
    for k, v in fish.items():
        if k == 0:
            new_fish[6] += v
            new_fish[8] += v
        else:
            new_fish[k - 1] += v
    fish = new_fish
print(sum(fish.values()))
