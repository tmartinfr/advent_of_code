from day_07 import get_outermost_bags, parse_input, count_inner_bags


data = parse_input(open('input_test.txt', 'r').readlines())
ret = get_outermost_bags(data, 'shiny gold')
assert set(ret) == set(['bright white', 'muted yellow', 'dark orange',
                        'light red'])


data = parse_input(open('input_test2.txt', 'r').readlines())
print(data)
ret = count_inner_bags(data, 'shiny gold')
assert ret == 126
