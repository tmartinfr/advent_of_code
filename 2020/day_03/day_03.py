def count_trees(forest, x_offset=3, y_offset=1):
    x = 0
    y = 0
    tree_num = 0
    while True:
        x = (x + x_offset) % (len(forest[0]))
        y += y_offset
        if y > (len(forest) - 1):
            break
        char = forest[y][x]
        # print(x, y, char)
        if char == '#':
            tree_num += 1
    return tree_num


if __name__ == '__main__':
    forest = [line.strip() for line in open('input.txt', 'r')]
    n = count_trees(forest)
    print(f'Number of trees : {n}')

    n2 = 1
    for offset in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        n2 *= count_trees(forest, offset[0], offset[1])
    print(f'Number of trees (part2) : {n2}')
