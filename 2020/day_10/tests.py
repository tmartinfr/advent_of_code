from day_10 import get_joltage_differences_count, resolve_part2, split_by_three


assert split_by_three([1, 2, 5, 7]) == [[1, 2], [5, 7]]

data1 = [int(num) for num in open('input_test_1', 'r')]
res = get_joltage_differences_count(data1)
assert res == {1: 7, 3: 5}

data2 = [int(num) for num in open('input_test_2', 'r')]
res = get_joltage_differences_count(data2)
assert res == {1: 22, 3: 10}

res = resolve_part2(data1)
assert res == 8

res = resolve_part2(data2)
assert res == 19208
