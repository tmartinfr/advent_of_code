from math import prod


def fill_basin(result, sizes):
    changed = True
    while changed:
        changed = False
        for y, line in enumerate(result):
            for x, d in enumerate(line):
                if result[y][x] != ".":
                    continue
                if bid := get_neighbour_basin_id(result, y, x):
                    result[y][x] = bid
                    sizes[bid] += 1
                    changed = True


def get_neighbour_basin_id(result, y, x):
    for delta_y, delta_x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        rel_y = y + delta_y
        rel_x = x + delta_x
        if rel_y < 0 or rel_x < 0:
            continue
        try:
            if isinstance(result[rel_y][rel_x], int):
                return result[rel_y][rel_x]
        except IndexError:
            continue


def is_lowest(area, y, x):
    height = area[y][x]
    for delta_y, delta_x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        rel_y = y + delta_y
        rel_x = x + delta_x
        if rel_y < 0 or rel_x < 0:
            continue
        try:
            if area[rel_y][rel_x] <= height:
                return False
        except IndexError:
            pass
    return True


def init_area(area, result, sizes):
    bid = 1
    for y, line in enumerate(area):
        for x, d in enumerate(line):
            if area[y][x] == 9:
                result[y][x] = "¤"
            elif is_lowest(area, y, x):
                result[y][x] = bid
                sizes[bid] = 1
                bid += 1


def print_area(area):
    print("\n".join(["".join([str(x) for x in y]) for y in area]))


area = [[int(d) for d in line.strip()] for line in open("09a_input", "r")]
result = [["." for _ in range(0, len(y))] for y in area]
sizes = {}
init_area(area, result, sizes)
fill_basin(result, sizes)
print(prod(sorted(sizes.values(), reverse=True)[:3]))
