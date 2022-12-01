def parse_input(lines):
    return [[parts[0], int(parts[1])] for line in lines if (parts := line.split(' '))]  # noqa


def compute_acc_before_loop(data):
    acc = 0
    ip = 0
    passed = [0]
    while True:
        ins, arg = data[ip]
        if ins == 'nop':
            ip += 1
        elif ins == 'acc':
            acc += arg
            ip += 1
        elif ins == 'jmp':
            ip += arg
        if ip in passed:
            return acc
        else:
            passed.append(ip)
        continue


class LoopException(Exception):
    pass


def compute_acc_after_patching(data, ip=0, acc=0, passed=None, patched=False):
    if not passed:
        passed = []

    if ip in passed:
        raise LoopException
    else:
        passed.append(ip)

    ins, arg = data[ip]

    if ins == 'nop':
        new_ip = ip + 1
    elif ins == 'acc':
        acc += arg
        new_ip = ip + 1
    elif ins == 'jmp':
        new_ip = ip + arg

    if new_ip >= len(data):
        return acc
    else:
        passed_copy = passed.copy()
        try:
            return compute_acc_after_patching(data, new_ip, acc, passed_copy, patched)
        except LoopException:
            if not patched:
                if ins == 'jmp':
                    new_ip = ip + 1
                elif ins == 'nop':
                    new_ip = ip + arg
                else:
                    raise LoopException
                if new_ip >= len(data):
                    return acc
                else:
                    return compute_acc_after_patching(data, new_ip, acc, passed_copy, True)
            else:
                raise LoopException



if __name__ == '__main__':
    data = parse_input(open('input.txt', 'r'))
    res = compute_acc_before_loop(data)
    print(f'Accumulator is {res} before infinite loop')

    res = compute_acc_after_patching(data)
    print(f'Accumulator is {res} after patching')
