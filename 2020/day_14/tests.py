from day_14 import parse_input, read_program, read_program_v2


def test_part1():
    data = parse_input('input_test')
    mem = read_program(data)
    assert sum(mem.values()) == 165


def test_part2():
    data = parse_input('input_test2')
    mem = read_program_v2(data)
    assert sum(mem.values()) == 208
