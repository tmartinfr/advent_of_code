from day_15 import get_nth_number


def test_part1():
    assert get_nth_number([0, 3, 6], 2020) == 436
    assert get_nth_number([1, 3, 2], 2020) == 1
    assert get_nth_number([2, 1, 3], 2020) == 10
    assert get_nth_number([1, 2, 3], 2020) == 27
    assert get_nth_number([2, 3, 1], 2020) == 78
    assert get_nth_number([3, 2, 1], 2020) == 438
    assert get_nth_number([3, 1, 2], 2020) == 1836


def test_part2():
    assert get_nth_number([0, 3, 6], 30_000_000) == 175594
    assert get_nth_number([1, 3, 2], 30_000_000) == 2578
    assert get_nth_number([2, 1, 3], 30_000_000) == 3544142
    assert get_nth_number([1, 2, 3], 30_000_000) == 261214
    assert get_nth_number([2, 3, 1], 30_000_000) == 6895259
    assert get_nth_number([3, 2, 1], 30_000_000) == 18
    assert get_nth_number([3, 1, 2], 30_000_000) == 362
