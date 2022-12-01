pos = [int(n) for n in open('07a_input', 'r').readline().strip().split(',')]
t = dict()
for n in range(0, max(pos) + 1):
    t[n] = sum([abs(p - n) for p in pos])
print(min(t.values()))
