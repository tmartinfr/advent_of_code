res = 0
for a, b in [line.strip().split(' | ') for line in open('08a_input', 'r').readlines()]:  # noqa: E501
    res += sum([1 for n in b.split() if len(n) in [2, 4, 3, 7]])
print(res)
