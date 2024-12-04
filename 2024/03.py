import sys


line = "".join([line.strip() for line in open(sys.argv[1]).readlines()])

def read_number(line, pos):
    number = ""
    rpos = 0
    for i in range(0, 3):
        c = line[pos+i]
        if not 48 <= ord(c) <= 57:
            break
        number += c
        rpos += 1
    return int(number), pos + rpos

def read_op(line, pos):
    cpos = pos
    next_pos = pos + 1

    if line[cpos:cpos+4] == "mul(":
        cpos += 4
    else:
        return None, next_pos

    number1, cpos = read_number(line, cpos)
    if not number1:
        return None, next_pos

    if line[cpos] != ",":
        return None, next_pos
    cpos += 1

    number2, cpos = read_number(line, cpos)
    if not number2:
        return None, next_pos

    if line[cpos] != ")":
        return None, next_pos
    cpos += 1

    print(f"mul({number1},{number2})")
    return number1 * number2, cpos

def check_do(line, pos):
    if line[pos:pos+4] == "do()":
        return True
    if line[pos:pos+7] == "don't()":
        return False

def compute(line, allow_do=False):
    pos = 0
    total_res = 0
    enabled = True
    while pos < len(line):
        if allow_do:
            _enabled = check_do(line, pos)
            if _enabled is not None:
                enabled = _enabled
            if not enabled:
                pos = pos + 1
                continue
        res, pos = read_op(line, pos)
        if res:
            total_res += res
    return total_res

print(compute(line))

print(compute(line, allow_do=True))
