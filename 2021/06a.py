num = [int(n) for n in open('06a_input').readline().strip().split(',')]
day = 0
while day < 80:
    day += 1
    new = []
    for i, n in enumerate(num):
        if n == 0:
            num[i] = 6
            new.append(8)
        else:
            num[i] -= 1
    num += new
print(len(num))
