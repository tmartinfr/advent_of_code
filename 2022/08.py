t = [[int(h) for h in l.strip()] for l in open('08_input')]
y_m = len(t) - 1
x_m = len(t[0]) - 1


def is_visible(y, x):
    tree_h = t[y][x]
    y_is_smaller_top = [t[y_p][x] < tree_h for y_p in range(0, y)]
    y_is_smaller_bottom = [t[y_p][x] < tree_h for y_p in range(y + 1, y_m + 1)]
    x_is_smaller_top = [t[y][x_p] < tree_h for x_p in range(0, x)]
    x_is_smaller_bottom = [t[y][x_p] < tree_h for x_p in range(x + 1, x_m + 1)]
    return all(y_is_smaller_top) or all(y_is_smaller_bottom) or all(x_is_smaller_top) or all(x_is_smaller_bottom)


def scenic_score(y, x):
    tree_h = t[y][x]

    score = 1

    s = 0
    for y_p in range(y - 1, -1, -1):
        s += 1
        if t[y_p][x] >= tree_h:
            break
    score *= s

    s = 0
    for y_p in range(y + 1, y_m + 1):
        s += 1
        if t[y_p][x] >= tree_h:
            break
    score *= s

    s = 0
    for x_p in range(x - 1, -1, -1):
        s += 1
        if t[y][x_p] >= tree_h:
            break
    score *= s

    s = 0
    for x_p in range(x + 1, x_m + 1):
        s += 1
        if t[y][x_p] >= tree_h:
            break
    score *= s

    return score


print(sum([1 if is_visible(y, x) else 0 for y in range(1, y_m) for x in range(1, x_m)]) + x_m * 2 + y_m * 2)

scenic_scores = [scenic_score(y, x) for y in range(0, y_m + 1) for x in range(0, x_m + 1)]
print(sorted(scenic_scores)[-1])
