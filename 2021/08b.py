from collections import defaultdict


ln = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}
ln = {frozenset(c): n for c, n in ln.items()}
nl = {n: c for c, n in ln.items()}

total = 0

for a, b in [line.strip().split(' | ') for line in open('08a_input', 'r').readlines()]:  # noqa: E501
    c = {}
    known = {}

    for digit in [frozenset(d) for d in a.split()]:
        m = k = None
        match len(digit):  # noqa: E999
            case 2:
                k = nl[1]
            case 3:
                k = nl[7]
            case 4:
                k = nl[4]
            case 5:
                m = [nl[2], nl[3], nl[5]]
            case 6:
                m = [nl[0], nl[6], nl[9]]
            case 7:
                k = nl[8]
        if k:
            known[digit] = k
        if m:
            c[digit] = m

    while len(known) < 10:

        new_c = defaultdict(list)
        for digit, candidates in c.items():
            for candidate in candidates:
                if candidate in known.values():
                    continue
                if any([k.issubset(digit) and not v.issubset(candidate) for k, v in known.items()]):  # noqa: E501
                    continue
                if any([digit.issubset(k) and not candidate.issubset(v) for k, v in known.items()]):  # noqa: E501
                    continue
                new_c[digit].append(candidate)
        c = new_c

        new_c = defaultdict(list)
        for digit, candidates in c.items():
            if len(candidates) == 1:
                known[digit] = candidates[0]
            else:
                new_c[digit] = candidates
        c = new_c

    total += int(''.join([str(ln[known[frozenset(digit)]]) for digit in b.split()]))  # noqa: E501

print(total)
