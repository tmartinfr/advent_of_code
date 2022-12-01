from day_18 import eval_expr, eval_expr2


def test_part1():
    assert eval_expr("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert eval_expr("2 * 3 + (4 * 5)") == 26
    assert eval_expr("2 * 3 + (4 * 5) * 1") == 26
    assert eval_expr("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert eval_expr("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert eval_expr("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert eval_expr("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    assert eval_expr("((3 + 8 + 3 * 6) + (2 + 5 * 7) * 4 + 6 + 7) + (2 + 3 * 6 * (7 + 2 + 7)) * 6 + 2") == 6152


def test_part2():
    assert eval_expr2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert eval_expr2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert eval_expr2("2 * 3 + (4 * 5)") == 46
    assert eval_expr2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert eval_expr2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert eval_expr2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
