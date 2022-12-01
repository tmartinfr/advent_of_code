from day_16 import (
    parse_input, parse_input_2, find_invalid_values, find_values_in_my_ticket)


def test_part2():
    data = parse_input('input_test')
    invalid_values = find_invalid_values(data)
    data2 = parse_input_2(data, invalid_values)
    assert find_values_in_my_ticket(data2) == {'class': 12, 'row': 11, 'seat': 13}
