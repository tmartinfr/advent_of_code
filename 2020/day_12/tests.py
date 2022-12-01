from . import move_to, parse_input, move_to_v2


def test_part1():
    data = parse_input('input_test')
    assert move_to(data) == [17, -8]


def test_part2():
    data = parse_input('input_test')
    assert move_to_v2(data) == [214, -72]
