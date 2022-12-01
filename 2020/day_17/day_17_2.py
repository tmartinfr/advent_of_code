from copy import deepcopy
from itertools import product


def display(grid):
    for wi, w in enumerate(grid):
        for zi, z in enumerate(w):
            print(f'z={zi}, w={wi}')
            for y in z:
                print(''.join(["#" if x else "." for x in y]))


def cycle(grid):
    len_grid = len(grid[0][0]) + 2

    for w in grid:
        for z in w:
            for y in z:
                expand_level(y, False)
            expand_level(z, [False] * len_grid)
        expand_level(w, [[False] * len_grid for _ in range(0, len_grid)])
    expand_level(grid, [[[False] * len_grid for _ in range(0, len_grid)] for _ in range(0, len_grid)])

    new_grid = deepcopy(grid)
    for wi, w in enumerate(grid):
        for zi, z in enumerate(w):
            for yi, y in enumerate(z):
                for xi, x in enumerate(y):
                    new_grid[wi][zi][yi][xi] = compute_cell(x, grid, wi, zi, yi, xi)
    return new_grid


def expand_level(level, elem):
    level.insert(0, elem)
    level.append(deepcopy(elem))


def is_alive(grid, w, z, y, x):
    try:
        return grid[w][z][y][x]
    except IndexError:
        return False


def compute_cell(state, grid, wi, zi, yi, xi):
    rel = list(product((-1, 0, 1), repeat=4))
    rel.remove((0, 0, 0, 0))
    neighbors = sum([1 for wri, zri, yri, xri in rel if is_alive(grid, wi + wri, zi + zri, yi + yri, xi + xri)])
    if state and neighbors not in (2, 3):
        state = False
    if not state and neighbors == 3:
        state = True
    return state


grid = [[[[char == "#" for char in line.strip()] for line in open('input.txt', 'r')]]]
print("Before any cycles:\n")
display(grid)

for n_cycle in range(1, 7):
    print(f"\n\nAfter {n_cycle} cycle(s):\n")
    grid = cycle(grid)
    display(grid)

res = sum([1 for w in grid for z in w for y in z for x in y if x])
print(f'Number of alive cubes in part 2 is {res}')
