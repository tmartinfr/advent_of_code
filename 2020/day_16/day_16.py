import collections
import itertools
import functools
import operator
import re


def parse_input(filename):
    data = {'rules': collections.OrderedDict(), 'your': None, 'nearby': []}
    with open(filename, 'r') as fd:
        while line := fd.readline():
            if line == "\n":
                break
            if m := re.match(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', line):
                data['rules'][m.group(1)] = [range(int(m.group(2)), int(m.group(3)) + 1), range(int(m.group(4)), int(m.group(5)) + 1)]  # noqa

        while line := fd.readline():
            if line.startswith('your ticket'):
                continue
            if line == "\n":
                break
            data['your'] = [int(value) for value in line.strip().split(',')]

        while line := fd.readline():
            if line.startswith('nearby ticket'):
                continue
            data['nearby'].append([int(value) for value in line.strip().split(',')])
    return data


def parse_input_2(data, invalid_values):
    data2 = {'rules': data['rules'], 'your': data['your'], 'tickets': [data['your']]}
    for n in data['nearby']:
        data2['tickets'].append([None if val in invalid_values else val for val in n])
    return data2


def find_invalid_values(data):
    def is_valid(value):
        for r in itertools.chain.from_iterable(data['rules'].values()):
            if value in r:
                return True

    return [value for value in itertools.chain.from_iterable(data['nearby']) if
            not is_valid(value)]


def find_values_in_my_ticket(data):
    columns = list(zip(*data['tickets']))
    rules_candidates = collections.defaultdict(list)
    for rule_index, rule_ranges in enumerate(data['rules'].values()):
        for column_index, column in enumerate(columns):
            if all([c in rule_ranges[0] or c in rule_ranges[1] or c is None for c in column]):
                rules_candidates[rule_index].append(column_index)
    rules_candidates = eliminate(rules_candidates)
    column_to_rule_index = {v: k for k, v in rules_candidates.items()}
    rules_names = list(data['rules'])
    res = {rules_names[column_to_rule_index[i]]: value for i, value in enumerate(data['your'])}
    print(res)
    return res


def eliminate(data):
    def display():
        for rule_index, columns in data.items():
            print(f'{rule_index}: {columns}')
    while any([isinstance(column, list) for column in data.values()]):
        smallest_index = [rule_index for rule_index, columns in data.items() if isinstance(columns, list) and len(columns) == 1][0]
        smallest_value = data[smallest_index][0]
        for rule_index, column in data.items():
            if rule_index == smallest_index:
                data[rule_index] = column[0]
            elif isinstance(data[rule_index], list):
                data[rule_index].remove(smallest_value)
        display()
    return data


if __name__ == '__main__':
    data = parse_input('input')
    invalid_values = find_invalid_values(data)
    res = sum(invalid_values)
    print(f'Total of invalid values for part1 is {res}')

    data2 = parse_input_2(data, invalid_values)
    values = find_values_in_my_ticket(data2)
    res = functools.reduce(operator.mul, [value for field, value in values.items() if field.startswith('departure')])
    print(f'Product for part2 is {res}')
