def get_nth_number(data, n):
    num = {}
    spoken = None

    for index, initial in enumerate(data):
        num[initial] = [index + 1]
        spoken = initial

    for turn in range(len(data) + 1, n+1):
        if len(num[spoken]) < 2:
            spoken = 0
        else:
            spoken = num[spoken][-1] - num[spoken][-2]

        if spoken in num:
            num[spoken].append(turn)
        else:
            num[spoken] = [turn]
    return spoken


if __name__ == '__main__':
    res = get_nth_number([0, 13, 1, 16, 6, 17], 2020)
    print(f'Part 1 result is {res}')

    res = get_nth_number([0, 13, 1, 16, 6, 17], 30000000)
    print(f'Part 2 result is {res}')
