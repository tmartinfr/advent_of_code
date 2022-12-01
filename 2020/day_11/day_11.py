from itertools import product


def parse_input(filename):
    return [line.strip() for line in open(filename, 'r')]


def print_data(data):
    for line in data:
        print(line)
    print()


def search_seat(data, line_index, cell_index, line_offset, cell_offset):
    if line_offset == 0 and cell_offset == 0:
        return None
    while True:
        line_index += line_offset
        cell_index += cell_offset
        if line_index < 0 or line_index > len(data) - 1 or cell_index < 0 or cell_index > len(data[0]) - 1:
            return None
        if data[line_index][cell_index] != '.':
            return data[line_index][cell_index]


def remote_adjacent(data, line_index, cell_index):
    directions = product([-1, 0, 1], [-1, 0, 1])
    return sum(
        [1 for d in directions
         if search_seat(data, line_index, cell_index, d[0], d[1]) == '#'])


def adjacent(data, line_index, cell_index):
    adjacents = ''

    if cell_index == 0:
        left = 0
    else:
        left = cell_index - 1
        adjacents += data[line_index][left]

    if cell_index == len(data[0]) - 1:
        right = len(data[0]) - 1
    else:
        right = cell_index + 1
        adjacents += data[line_index][right]

    if line_index != 0:
        adjacents += data[line_index - 1][left:right+1]

    if line_index != len(data) - 1:
        adjacents += data[line_index + 1][left:right+1]

    return sum([1 for cell in adjacents if cell == '#'])


def roundify(data, become_empty=4, check_remote_adjacent=False):
    def comp_cell(line_index, cell_index, cell):
        if cell == '.':
            return '.'

        if check_remote_adjacent:
            adjacent_func = remote_adjacent
        else:
            adjacent_func = adjacent

        if cell == '#' and adjacent_func(data, line_index, cell_index) >= become_empty:
            return 'L'

        if cell == 'L' and adjacent_func(data, line_index, cell_index) == 0:
            return '#'

        return cell

    def comp_line(line_index, line):
        return ''.join([comp_cell(line_index, cell_index, cell)
                       for cell_index, cell in enumerate(line)])

    return [comp_line(index, line)
            for index, line in enumerate(data)]


if __name__ == '__main__':
    prev_data = parse_input('input')
    count = 0
    while True:
        count += 1
        new_data = roundify(prev_data, become_empty=5, check_remote_adjacent=True)
        if prev_data == new_data:
            print('This was the last !')
            break
        print(f'Round {count}')
        print('=====')
        print_data(new_data)
        prev_data = new_data
    num = sum([1 for line in new_data for cell in line if cell == '#'])
    print(f'Number of occuped seats is {num}')
