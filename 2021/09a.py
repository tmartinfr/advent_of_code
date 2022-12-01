def get_point_score(y, x):
    height = area[y][x]
    for delta_y, delta_x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        rel_y = y + delta_y
        rel_x = x + delta_x
        if rel_y < 0 or rel_x < 0:
            continue
        try:
            if area[rel_y][rel_x] <= height:
                return 0
        except IndexError:
            pass
    return height + 1


area = [[int(d) for d in line.strip()] for line in open('09a_input', 'r')]
res = sum([
    get_point_score(y, x)
    for y, line in enumerate(area) for x, _ in enumerate(line)
])
print(res)
