def is_valid_password(range, letter, password):
    (min, max) = [int(digit) for digit in range.split('-')]
    letter_occurrences = 0
    for char in password:
        if char == letter:
            letter_occurrences += 1
    if letter_occurrences >= min and letter_occurrences <= max:
        return True
    else:
        return False


def is_valid_password_2(positions, letter, password):
    (is_at_first, is_at_second) = [password[int(digit)-1] == letter
                                   for digit in positions.split('-')]
    return is_at_first ^ is_at_second


if __name__ == '__main__':
    valid = 0
    valid2 = 0
    for line in open('input.txt', 'r'):
        (a, password) = line.split(': ')
        (range, letter) = a.split(' ')
        if is_valid_password(range, letter, password):
            valid += 1
        if is_valid_password_2(range, letter, password):
            valid2 += 1
    print(f'Number of valid passwords : {valid}')
    print(f'Number of valid passwords (part 2) : {valid2}')
