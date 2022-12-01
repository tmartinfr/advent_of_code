from day_08 import parse_input, compute_acc_before_loop, compute_acc_after_patching  # noqa


data = parse_input(open('input_test.txt', 'r'))
assert data == [['nop', 0], ['acc', 1], ['jmp', 4], ['acc', 3], ['jmp', -3],
                ['acc', -99], ['acc', 1], ['jmp', -4], ['acc', 6]]
assert compute_acc_before_loop(data) == 5
assert compute_acc_after_patching(data) == 8
