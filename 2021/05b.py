from itertools import zip_longest


def print_windmap(windmap):
    for line in windmap:
        print(''.join([str(c) for c in line]))


winds = [([int(n) for n in s[0].split(',')], [int(n) for n in s[1].split(',')]) for line in open('05a_input', 'r').readlines() if (s := line.strip().split(' -> '))]  # noqa: E501
x_len = max([c[0] for w in winds for c in w]) + 1
y_len = max([c[1] for w in winds for c in w]) + 1
windmap = [[0] * x_len for _ in range(0, y_len)]
for c1, c2 in winds:
    fill = None

    if c1[0] == c2[0]:
        fill = c1[0]
        rx = []
    elif c1[0] < c2[0]:
        rx = range(c1[0], c2[0] + 1)
    else:
        rx = range(c1[0], c2[0] - 1, -1)

    if c1[1] == c2[1]:
        fill = c1[1]
        ry = []
    elif c1[1] < c2[1]:
        ry = range(c1[1], c2[1] + 1)
    else:
        ry = range(c1[1], c2[1] - 1, -1)

    for x, y in zip_longest(rx, ry, fillvalue=fill):
        windmap[y][x] += 1


print(len([s for line in windmap for s in line if s >= 2]))
