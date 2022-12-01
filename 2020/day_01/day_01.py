def if_sum_multiply(numbers, target):
    for n1 in numbers:
        numbers_ = numbers.copy()
        numbers_.remove(n1)
        for n2 in numbers_:
            if n1 + n2 == target:
                return n1 * n2

def if_sum_multiply_3(numbers, target):
    for n1 in numbers:
        numbers2 = numbers.copy()
        numbers2.remove(n1)
        for n2 in numbers2:
            numbers3 = numbers2.copy()
            numbers3.remove(n2)
            for n3 in numbers2:
                if n1 + n2 + n3 == target:
                    return n1 * n2 * n3


if __name__ == '__main__':
    numbers = [int(number) for number in open('input', 'r')]

    result1 = if_sum_multiply(numbers, 2020)
    print(f'Result for part 1 is {result1}')

    result2 = if_sum_multiply_3(numbers, 2020)
    print(f'Result for part 2 is {result2}')
