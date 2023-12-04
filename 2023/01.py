NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

R_NUMBERS = {"".join(reversed(nl)):nn for nl, nn in NUMBERS.items()}

def get_first_number(chars, reverse=False):
    if reverse:
        chars = reversed(chars)
    for char in chars:
        if 47 < ord(char) < 58:
            return char

def get_first_number2(chars, reverse=False):
    chars_len = len(chars)
    chars = chars if not reverse else "".join(reversed(chars))
    numbers = NUMBERS if not reverse else R_NUMBERS

    for pos, char in enumerate(chars):
        if 47 < ord(char) < 58:
            return char
        extra_len = chars_len - pos
        for nl, nn in numbers.items():
            len_nl = len(nl)
            if len_nl > extra_len:
                continue
            if chars[pos:pos+len_nl] == nl:
                return nn

def get_calibration_value(line, func):
    first_number = func(line)
    last_number = func(line, reverse=True)
    return int(first_number + last_number)

lines = open("01_input").readlines()
result = sum([get_calibration_value(line.strip(), get_first_number) for line in lines])
print(result)
result = sum([get_calibration_value(line.strip(), get_first_number2) for line in lines])
print(result)
