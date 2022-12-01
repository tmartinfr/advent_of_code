
def find(lines, less_common=False):
    i = 0
    while (numlines := len(lines)) > 1:
        col = list(zip(*lines))[i]
        bit = '1' if col.count('1') >= numlines / 2 else '0'
        if less_common:
            bit = '0' if bit == '1' else '1'
        lines = [line for line in lines if line[i] == bit]
        i += 1
    return int(lines[0], 2)


lines = [line.strip() for line in open('03a_input').readlines()]
oxygen = find(lines)
co2 = find(lines, True)
print(oxygen * co2)
