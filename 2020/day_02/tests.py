from day_02 import *

assert not is_valid_password('1-3', 'g', 'abc')
assert is_valid_password('1-3', 'g', 'agbc')
assert not is_valid_password('1-3', 'g', 'agbcggg')

assert not is_valid_password_2('1-3', 'a', 'aba')
assert is_valid_password_2('1-3', 'a', 'abx')
assert not is_valid_password_2('1-3', 'a', 'xbx')
