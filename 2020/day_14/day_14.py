import itertools
import re

from loguru import logger


def parse_input(filename):
    data = []
    for line in open(filename, 'r'):
        if m := re.match(r'mem\[(\d+)\] = (\d+)$', line):
            data.append({'op': 'mem', 'value': {'addr': int(m.group(1)), 'value': int(m.group(2))}})
        elif m := re.match(r'mask = ([X\d]+)', line):
            data.append({'op': 'mask', 'value': m.group(1)})
    return data


def read_program(data):
    mask = None
    mem = {}
    ascii_mask = None
    for ins in data:
        op = ins['op']
        value = ins['value']
        if op == 'mem':
            addr = value['addr']
            value = value['value']
            logger.info(f'pre-value  : {value:12} ({value:036b})')
            logger.info(f'mask is :                  {ascii_mask}')
            if mask:
                logger.info(f'applying and mask :        {mask[0]:036b}')
                value &= mask[0]
                logger.info(f'applying or mask :         {mask[1]:036b}')
                value |= mask[1]
            logger.info(f'post-value : {value:12} ({value:036b})')
            mem[addr] = value
        elif op == 'mask':
            ascii_mask = value
            mask = compute_mask(ascii_mask)
    return mem


def read_program_v2(data):
    mem = {}
    mask = None
    for ins in data:
        op = ins['op']
        value = ins['value']
        if op == 'mem':
            addr = write_mem(mem, value['addr'], mask, value['value'] )
        elif op == 'mask':
            mask = list(value)
            mask.reverse()
            logger.info(f'new mask : {mask}')
    return mem


def write_mem(mem, addr, mask, value):
    floating = []
    for index, bit in enumerate(mask):
        if bit == 'X':
            floating.append(index)
        elif bit == '1':
            addr |= 1<<index
    for bits in itertools.product((0, 1), repeat=len(floating)):
        _addr = addr
        for index, bit_index in enumerate(floating):
            if bits[index]:
                _addr |= 1<<bit_index
            else:
                m = int('1'*36, 2)
                m ^= 1<<bit_index
                _addr &= m
        mem[_addr] = value


def compute_mask(value):
    logger.info(f'computing mask {value}')
    and_mask = or_mask = 0
    mask = list(value)
    mask.reverse()
    for index, bit in enumerate(mask):
        if bit == 'X':
            and_mask |= 1<<index
        elif bit == '1':
            and_mask |= 1<<index
            or_mask |= 1<<index
    return (and_mask, or_mask)


if __name__ == '__main__':
    data = parse_input('input')

    mem = read_program(data)
    res = sum(mem.values())
    print(f'Result for part1 is {res}')

    mem = read_program_v2(data)
    res = sum(mem.values())
    print(f'Result for part2 is {res}')
