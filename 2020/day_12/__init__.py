import operator


def parse_input(filename):
    return [(line[0], int(line[1:])) for line in open(filename, 'r')]


CARDINALS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

ROTATE = {
    'L': -1,
    'R': 1,
}

CAP = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}


def compute_position(pos, offset, value):
    full_offset = map(operator.mul, offset, (value, value))
    pos = map(operator.add, pos, full_offset)
    return list(pos)


def move_to(instructions):
    pos = [0, 0]
    direction = 90
    for ins, value in instructions:
        if ins in CARDINALS:
            pos = compute_position(pos, CARDINALS[ins], value)
        elif ins in ROTATE:
            direction += (ROTATE[ins] * value)
            direction %= 360
        elif ins == 'F':
            print(direction)
            pos = compute_position(pos, CARDINALS[CAP[direction]], value)
    return pos


def rotate_waypoint(waypoint, direction, value):
    angle = direction * value
    if angle < 0:
        angle += 360
    if angle == 90:
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    if angle == 180:
        waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
    if angle == 270:
        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    return waypoint


def move_to_v2(instructions):
    pos = [0, 0]
    waypoint = [10, 1]
    for ins, value in instructions:
        if ins in CARDINALS:
            waypoint = compute_position(waypoint, CARDINALS[ins], value)
        elif ins in ROTATE:
            waypoint = rotate_waypoint(waypoint, ROTATE[ins], value)
        elif ins == 'F':
            pos = compute_position(pos, waypoint, value)
    return pos


if __name__ == '__main__':
    data = parse_input('input')

    pos = move_to(data)
    distance = abs(pos[0]) + abs(pos[1])
    print(f'Distance is {distance}')

    pos_v2 = move_to_v2(data)
    distance = abs(pos_v2[0]) + abs(pos_v2[1])
    print(f'Distance (v2) is {distance}')
