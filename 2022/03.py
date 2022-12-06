def sum_priorities(common):
    return sum([ord(c) - (96 if c.islower() else 38) for s in common if (c := list(s)[0])])

lines = open('03_input').readlines()
data = [(line[:llen//2], line[llen//2:llen]) for line in lines if (llen := len(line.strip()))]
common = [set(t[0]) & set(t[1]) for t in data]
print(sum_priorities(common))

common = []
for i in range(0, len(lines), 3):
    common.append(set(lines[i].strip()) & set(lines[i+1].strip()) & set(lines[i+2].strip()))
print(sum_priorities(common))
