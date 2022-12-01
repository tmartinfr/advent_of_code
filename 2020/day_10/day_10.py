import networkx as nx


def get_joltage_differences_count(data):
    data.sort()
    differences = {}
    for index, num in enumerate(data):
        if index == 0:
            diff = num
        else:
            diff = num - data[index - 1]
        assert 0 < diff < 4
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1
    differences[3] += 1
    return differences


def count_arrangements(data):
    if len(data) == 1:
        return 1
    G = nx.DiGraph()
    for num in data:
        G.add_node(num)
    for num in data:
        for candidate in range(num + 1, num + 4):
            if candidate in data:
                G.add_edge(num, candidate)
    count = 0
    for path in nx.all_simple_edge_paths(G, min(data), max(data)):
        count += 1
    return count


def split_by_three(data):
    res = []
    cur = []
    for index, num in enumerate(data):
        cur.append(num)
        if index == len(data) - 1 or data[index + 1] >= num + 3:
            res.append(cur)
            cur = []
    return res


def resolve_part2(data):
    data.insert(0, 0)
    data.append(max(data) + 3)
    data_seg = split_by_three(data)
    res = 1
    for data in data_seg:
        res *= count_arrangements(data)
    return res


if __name__ == '__main__':
    data = [int(num) for num in open('input', 'r')]

    differences = get_joltage_differences_count(data)
    res = differences[1] * differences[3]
    print(f'Part 1 result is {res}')

    res = resolve_part2(data)
    print(f'Part 2 result is {res}')
