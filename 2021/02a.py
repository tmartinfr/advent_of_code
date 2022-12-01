ins = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1),
}
moves = [
    [x * int(n) for x in ins[i]]
    for i, n
    in [line.strip().split(' ') for line in open('02a_input').readlines()]
]
forward = sum(m[0] for m in moves)
depth = sum(m[1] for m in moves)
print(forward * depth)
