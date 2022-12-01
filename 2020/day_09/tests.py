from day_09 import first_invalid, find_add_range_min_max


data = [int(num.strip()) for num in open('input_test', 'r')]
res = first_invalid(data, preambule_length=5)
assert res == 127

assert find_add_range_min_max(data, res) == (15, 47)
