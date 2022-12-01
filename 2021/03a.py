lines = [line.strip() for line in open('03a_input').readlines()]
numlines = len(lines)
vnum = [int(''.join(s), 2) for s in zip(*lines)]

gamma = epsilon = 0
for n in vnum:
    gamma <<= 1
    epsilon <<= 1
    if bin(n).count('1') > numlines / 2:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
