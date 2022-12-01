groups = []
answers = None

for line in open('input', 'r'):
    if answers is None:
        answers = set()
        groups.append(answers)

    if line == "\n":
        answers = None
        continue

    for answer in line.strip():
        answers.add(answer)

total = 0
for answers in groups:
    total += len(answers)

print(f'Sum of answers is : {total}')

groups = []
answers = None

for line in open('input', 'r'):
    if answers is None:
        answers = {}
        answers['count'] = 0
        groups.append(answers)
        people_count = 0

    if line == "\n":
        answers = None
        people_count = None
        continue

    answers['count'] += 1

    for answer in line.strip():
        if answer in answers:
            answers[answer] += 1
        else:
            answers[answer] = 1

total = 0
for answers in groups:
    print(answers)
    for answer, count in answers.items():
        if answer == 'count':
            continue
        if count == answers['count']:
            total += 1

print(f'Sum of answers (part 2) is : {total}')
