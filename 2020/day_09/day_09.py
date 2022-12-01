def first_invalid(data, preambule_length=25):
    _range = range(preambule_length, len(data) - 1)
    for index in _range:
        num = data[index]
        found = False
        for num1 in data[index-25:index]:
            for num2 in data[index-25:index]:
                if (num1 + num2 == num) and (num1 != num2):
                    found = (num1, num2)
                    break
        if not found:
            return num


def find_add_range_min_max(data, res):
    def find_add_range(start_index, cur=0):
        cur += data[start_index]
        if cur < res:
            r = find_add_range(start_index + 1, cur)
            if r:
                return [data[start_index]] + r
            else:
                return None
        elif cur == res:
            return [data[start_index]]
        elif cur > res:
            return None
        else:
            raise AssertionError('should not happen')

    for index in range(0, data.index(res) - 2):
        ret = find_add_range(index)
        if ret:
            return (min(ret), max(ret))
    raise Exception('not found !')


if __name__ == '__main__':
    data = [int(num.strip()) for num in open('input', 'r')]
    res = first_invalid(data)
    print(f'First invalid is {res}')

    (min, max) = find_add_range_min_max(data, res)
    sum = min + max
    print(f'Add range min is {min}, max is {max}, sum is {sum}')
