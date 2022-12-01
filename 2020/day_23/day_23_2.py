from itertools import chain


cups_input = "364289715"
node_number = 1_000_000
moves = 10_000_000

def append(cups, label, labels):
    orig_next = cups[label]

    cur = label
    for l in labels:
        cups[cur] = l
        cur = l

    cups[cur] = orig_next

def pick_next(cups, current):
    cur = cups[current]
    for _ in range(0, 3):
        yield cur
        n = cups[cur]
        del cups[cur]
        cur = n
    cups[current] = n

def find_dest(cups, current, node_number):
    for i in chain(range(current - 1, 0, -1), range(node_number, current, -1)):
        if i in cups:
            return i

cups = {}
current = None
for i, char in enumerate(cups_input):
    label = int(char)

    if not current:
        current = label

    if i == len(cups_input) - 1:
        next_label = current
    else:
        next_label = int(cups_input[i + 1])

    cups[label] = next_label

append(cups, label, [i for i in range(10, node_number + 1)])

for move in range(1, moves + 1):
    print(f'-- move {move} --')
    picked = list(pick_next(cups, current))
    print(f'current : {current}')
    print(f'picked : {picked}')
    dest = find_dest(cups, current, node_number)
    print(f'destination : {dest}')
    append(cups, dest, picked)
    current = cups[current]

first_star = cups[1]
second_star = cups[first_star]
print(first_star * second_star)
