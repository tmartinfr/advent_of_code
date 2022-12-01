def compute_seat_id(code):
    row_code, column_code = code[:7], code[7:10]

    min, max = 0, 127
    for c in row_code:
        middle_minus = ((min + max) / 2) - 0.5
        if c == 'F':
            max = middle_minus
        elif c == 'B':
            min = middle_minus + 1
    assert min == max
    res = min * 8

    min, max = 0, 7
    for c in column_code:
        middle_minus = ((min + max) / 2) - 0.5
        if c == 'L':
            max = middle_minus
        elif c == 'R':
            min = middle_minus + 1
    assert min == max
    res += min

    return int(res)


if __name__ == "__main__":
    seat_ids = [compute_seat_id(code.strip())
                for code in open('input', 'r')]
    max_seat_id = max(seat_ids)
    print(f'Max seat ID is : {max_seat_id}')

    absolute_max_seat_id = 127*7 + 7
    for seat_id in range(0, absolute_max_seat_id):
        if seat_id not in seat_ids and seat_id+1 in seat_ids and seat_id-1 in seat_ids:
            print(f'My seat is {seat_id}')
