def is_valid(passport):
    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if set([key for key in passport.keys() if key != 'cid']) == required:
        return True
    return False


def is_valid_2(passport):
    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if set([key for key in passport.keys() if key != 'cid']) != required:
        return False

    try:
        byr = int(passport['byr'])
        if byr < 1920 or byr > 2002:
            return False
    except ValueError:
        return False

    try:
        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False
    except ValueError:
        return False

    try:
        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False
    except ValueError:
        return False

    hgt = passport['hgt']
    if not (hgt.endswith('in') or hgt.endswith('cm')):
        return False
    try:
        num = int(hgt[:-2])
        unit = hgt[-2:]
        if unit == 'cm' and (num < 150 or num > 193):
            return False
        if unit == 'in' and (num < 59 or num > 76):
            return False
    except ValueError:
        return False

    hcl = passport['hcl']
    if len(hcl) != 7:
        return False
    if not hcl.startswith('#'):
        return False
    for char in hcl[1:]:
        if char not in '0123456789abcdef':
            return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl',
                               'oth']:
        return False

    pid = passport['pid']
    try:
        int(pid)
    except ValueError:
        return False
    if len(pid) != 9:
        return False
    # if not pid.startswith('0'):
    #     return False

    return True


if __name__ == '__main__':
    passports = []
    passport = None
    for line in open('input.txt', 'r'):
        if passport is None or line == "\n":
            passport = {}
            passports.append(passport)
            continue
        for info in line.strip().split(' '):
            field, value = info.split(':')
            passport[field] = value
    number_valid = len([passport for passport in passports if
                        is_valid(passport)])
    print(f'There are {number_valid} valid passports')
    number_valid_2 = len([passport for passport in passports if
                         is_valid_2(passport)])
    print(f'There are {number_valid_2} (part 2) valid passports')
