from day_11 import parse_input, remote_adjacent, adjacent


data = parse_input('input_test_sample1')
assert adjacent(data, 4, 3) == 2
assert remote_adjacent(data, 4, 3) == 8

data = parse_input('input_test_sample2')
assert adjacent(data, 1, 1) == 0
assert remote_adjacent(data, 4, 3) == 0

data = parse_input('input_test_sample3')
assert adjacent(data, 3, 3) == 0
assert remote_adjacent(data, 3, 3) == 0
