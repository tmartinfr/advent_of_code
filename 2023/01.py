def get_calibration_value(line):
    def get_first_number(chars):
        for char in chars:
            if 47 < ord(char) < 58:
                return char
    first_number = get_first_number(line)
    last_number = get_first_number(reversed(line))
    return int(first_number + last_number)

lines = open("01_input").readlines()
result = sum([get_calibration_value(line.strip()) for line in lines])
print(result)
