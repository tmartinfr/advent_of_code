ins = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1),
}
moves = [
    [x * int(s[1]) for x in ins[s[0]]]
    for line
    in open('02a_input').readlines()
    if (s := line.split(' '))
]
aim = forward = depth = 0
for f, d in moves:
    if f:
        forward += f
        if aim:
            depth += f * aim
    elif d:
        aim += d
print(forward * depth)
