import itertools
import re


def parse_input(filename):
    fd = open(filename, 'r')
    rules = {}
    while line := fd.readline():
        if line == "\n":
            break
        rulenum, rulespec = line.strip().split(": ")
        if rulespec.startswith('"'):
            elem = rulespec[1]
        else:
            elem = [[]]
            for subspec in rulespec.split(" "):
                try:
                    elem[-1].append(int(subspec))
                except ValueError:
                    assert subspec == "|"
                    elem.append([])
        rules[int(rulenum)] = elem

    return (rules, [line.strip() for line in fd])


def get_regex(rules, num):
    def get_subregex(rule):
        if isinstance(rule, str):
            return rule
        else:
            reg = "|".join([''.join([get_subregex(rules[elem]) for elem in subrule]) for subrule in rule])
            return f'({reg})'


    return '^' + get_subregex(rules[num]) + '$'


(rules, messages) = parse_input('input')
matched = {}

def match(rules, messages, matched):
    reg = get_regex(rules, 0)
    for index, message in enumerate(messages):
        if index in matched:
            continue
        if m := re.match(reg, message):
            matched[index] = 1
            print(f"✓ {message}")

match(rules, messages, matched)
print(f'Answer for part1 is {len(matched)}')

it = itertools.product(range(1, 10), repeat=2)
for mul1, mul2 in it:
    rules[8] = [[42] * mul1]
    rules[11] = [[42] * mul2 + [31] * mul2]
    match(rules, messages, matched)

print(f'Answer for part2 is {len(matched)}')
