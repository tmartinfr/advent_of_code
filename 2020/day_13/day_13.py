import itertools
import functools
import operator


def parse_input(filename):
    fd = open(filename, 'r')
    return [int(fd.readline()), [int(busid) if busid != 'x' else None
            for busid in fd.readline().split(',')]]


def part1(earliest, buses):
    res = []
    for busid in buses:
        if not busid:
            continue
        timeto = (((earliest // busid) + 1) * busid) - earliest
        if not res or timeto < res[1]:
            res = [busid, timeto]
    return res


def part2(buses):
    buses = {busid: offset for offset, busid in enumerate(buses) if busid}

    def is_valid(ts):
        for busid, offset in buses.items():
            if (ts + offset) % busid:
                return False
        return True

    largest = max(buses)
    for ts in itertools.count(start=largest, step=largest):
        origin_ts = ts - buses[largest]
        if is_valid(origin_ts):
            return origin_ts


def part2_v2(buses):
    data = {busid: busid - offset for offset, busid in enumerate(buses) if
            busid}
    res = 0
    # Théorème chinois des restes
    # https://www.apprendre-en-ligne.net/crypto/rabin/mvc.pdf
    M = functools.reduce(operator.mul, data.keys())
    for modulo, rest in data.items():
        Mi = M // modulo
        yi = 1
        while (yi * Mi) % modulo != 1:
            yi += 1
        res += rest * Mi * yi
    return res % M


if __name__ == '__main__':
    data = parse_input('input')

    busid, timeto = part1(*data)
    res = busid * timeto
    print(f'Can leave with bus {busid} after waiting for {timeto}, '
          f'res is {res}')

    res = part2_v2(data[1])
    print(f'Earliest timestamp for part2 is {res}')
