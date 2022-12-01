from day_04 import is_valid


assert is_valid({'byr': 1, 'iyr': 1, 'eyr': 1, 'hgt': 1, 'hcl': 1, 'ecl': 1,
                 'pid': 1, 'cid': 1})
assert not is_valid({'iyr': 1, 'eyr': 1, 'hgt': 1, 'hcl': 1, 'ecl': 1, 'pid':
                     1, 'cid': 1})
assert is_valid({'byr': 1, 'iyr': 1, 'eyr': 1, 'hgt': 1, 'hcl': 1, 'ecl': 1,
                 'pid': 1})
