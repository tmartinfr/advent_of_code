import sys
from uuid import uuid4
from loguru import logger


WHITE = 1
BLACK = -1
DIRECTIONS = {
    'e': (-1, 1),
    'w': (1, -1),
    'se': (0, 1),
    'nw': (0, -1),
    'sw': (1, 0),
    'ne': (-1, 0),
}


def parse_input(filename):
    for line in open(filename, 'r'):
        line = line.strip()
        ret = []
        index = 0
        while index < len(line):
            for direction in [*DIRECTIONS]:
                if line[index:].startswith(direction):
                    ret.append(direction)
                    index += len(direction)
        yield ret

def compute_coor(coor, offset):
    return tuple([a[0] + a[1] for a in zip(coor, offset)])

def gen(tiles):
    new_tiles = {}

    def get_color(coor, current_color, create):
        if create:
            for d in DIRECTIONS.values():
                d_coor = compute_coor(coor, d)
                if not d_coor in tiles:
                    new_tiles[d_coor] = get_color(d_coor, WHITE, False)

        num_black = 0
        for d in DIRECTIONS.values():
            d_coor = compute_coor(coor, d)
            num_black += 1 if d_coor in tiles and tiles[d_coor] == BLACK else 0

        if current_color == BLACK and (num_black == 0 or num_black > 2):
            logger.debug(f'{coor} set to white')
            return WHITE
        elif current_color == WHITE and num_black == 2:
            logger.debug(f'{coor} set to black')
            return BLACK
        return current_color

    for coor, color in tiles.items():
        new_tiles[coor] = get_color(coor, color, True)

    return new_tiles

def count_black(tiles):
    return sum([1 for tile, color in tiles.items() if color == BLACK])

data = parse_input(sys.argv[1])

tiles = {}
tiles[(0, 0)] = WHITE

for ins in data:
    logger.info(f'Following instructions : {ins}')
    coor = [0, 0]
    for i in ins:
        offset = DIRECTIONS[i]
        coor = compute_coor(coor, offset)
        logger.debug(f'Getting offset {offset}, moving to {coor}')
    if coor in tiles:
        logger.info(f'Switching tile at {coor}')
        tiles[coor] *= -1
    else:
        logger.info(f'Creating new black tile at {coor}')
        tiles[coor] = BLACK

print(count_black(tiles))

for day in range(1, 101):
    tiles = gen(tiles)
    print(f'Day {day} : {count_black(tiles)} black tiles on a total of {len(tiles)}')
