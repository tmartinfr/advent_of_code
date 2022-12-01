import operator


OP = {
    '+': operator.add,
    '*': operator.mul,
}


def parse_input(data):

    def parse(units, level=0):
        expr = []
        it = enumerate(units)
        for index, unit in it:
            if unit.startswith('('):
                units[index] = unit[1:]
                sub_expr, j, nr = parse(units[index:], level + 1)
                expr.append(sub_expr)
                if nr > 0:
                    return (expr, index + j, nr - 1)
                for _ in range(0, j):
                    next(it, None)
                    index += 1
            elif unit in OP:
                expr.append(OP[unit])
            else:
                if unit.endswith(')'):
                    par_index = unit.index(')')
                    expr.append(int(unit[:par_index]))
                    return (expr, index, int(len(unit[par_index:])) - 1)
                expr.append(int(unit))
        return (expr, index)

    units = data.split(' ')
    return parse(units)[0]


def eval_expr(data):
    expr = parse_input(data)
    return compute_expr(expr)


def eval_expr2(data):
    def group_additions(expr):
        new_expr = []
        it = enumerate(expr)
        for index, unit in it:
            if len(expr) != 3 and index < (len(expr) - 1) and expr[index + 1] is operator.add:
                new_expr.append(group_additions(expr[index:index+3]))
                for _ in range(0, 2):
                    next(it, None)
            elif isinstance(unit, list):
                new_expr.append(group_additions(unit))
            else:
                new_expr.append(unit)

        return new_expr

    expr = parse_input(data)
    while (new_expr := group_additions(expr)) != expr:
        expr = new_expr
    return compute_expr(expr)


def compute_expr(expr):
    next_op = None
    result = None

    for unit in expr:
        if isinstance(unit, int):
            if result is None:
                result = unit
            else:
                result = next_op(result, unit)
        elif isinstance(unit, list):
            if result is None:
                result = compute_expr(unit)
            else:
                result = next_op(result, compute_expr(unit))
        else:
            next_op = unit

    return result


if __name__ == '__main__':
    total = 0
    for line in open('input.txt', 'r'):
        line = line.strip()
        res = eval_expr(line)
        # print(f'{line} = {res}')
        total += res
    print(f'Result for part1 is {total}')

    res2 = sum([eval_expr2(expr.strip()) for expr in open('input.txt', 'r')])
    print(f'Result for part1 is {res2}')
