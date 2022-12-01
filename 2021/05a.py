def print_windmap(windmap):
    for line in windmap:
        print(''.join([str(c) for c in line]))


winds = [([int(n) for n in s[0].split(',')], [int(n) for n in s[1].split(',')]) for line in open('05a_input', 'r').readlines() if (s := line.strip().split(' -> '))]  # noqa: E501
x_len = max([c[0] for w in winds for c in w]) + 1
y_len = max([c[1] for w in winds for c in w]) + 1
windmap = [[0] * x_len for _ in range(0, y_len)]
for c1, c2 in winds:
    if c1[0] == c2[0]:
        x = c1[0]
        r = sorted([c1[1], c2[1]])
        for y in range(r[0], r[1] + 1):
            windmap[y][x] += 1
    elif c1[1] == c2[1]:
        y = c1[1]
        r = sorted([c1[0], c2[0]])
        for x in range(r[0], r[1] + 1):
            windmap[y][x] += 1

print(len([s for line in windmap for s in line if s >= 2]))
