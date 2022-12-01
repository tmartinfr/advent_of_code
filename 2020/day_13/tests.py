from day_13 import part1, parse_input, part2_v2


data = parse_input('input_test')


def test_part1():
    assert part1(*data) == [59, 5]


def test_part2():
    assert part2_v2(data[1]) == 1068781
    assert part2_v2([17, None, 13, 19]) == 3417
    assert part2_v2([67, 7, 59, 61]) == 754018
    assert part2_v2([67, None, 7, 59, 61]) == 779210
    assert part2_v2([67, 7, None, 59, 61]) == 1261476
    assert part2_v2([1789, 37, 47, 1889]) == 1202161486
