from collections import defaultdict
from itertools import product
from functools import reduce
from operator import mul
import sys


VARIANTS = list(product((0, 90, 180, 270), (0, 1, 2)))
EDGE_RELATIONS = {
    "top": "bottom",
    "right": "left",
    "bottom": "top",
    "left": "right",
}


def rotate_data(data, angle):
    if angle == 0:
        return data
    elif angle == 90:
        return list([list(reversed(line)) for line in zip(*data)])
    elif angle == 180:
        return [list(reversed(line)) for line in reversed(data)]
    elif angle == 270:
        return list([line for line in reversed(list(zip(*data)))])


def flip_data(data, flip):
    if flip == 1:
        return list([list(reversed(line)) for line in data])
    elif flip == 2:
        return list([line for line in reversed(data)])
    else:
        return data


class Tile:
    tile_id = None
    data = None

    def __repr__(self):
        return self.tile_id

    def __init__(self, tile_id, data):
        self.tile_id = tile_id
        self.data = data

    def get_positioned(self, angle=0, flip=0):
        return PositionedTile(self, angle, flip)


class PositionedTile:
    tile = None
    angle = None
    flip = None
    top = None
    right = None
    bottom = None
    left = None

    def __repr__(self):
        return f"{self.tile_id} ({self.angle}, {self.flip})"

    def __init__(self, tile, angle, flip):
        self.tile = tile
        self.angle = angle
        self.flip = flip

    @property
    def tile_id(self):
        return self.tile.tile_id

    @property
    def edges(self):
        return {
            "top": self.data[0],
            "right": "".join([line[-1] for line in self.data]),
            "bottom": self.data[-1],
            "left": "".join([line[0] for line in self.data]),
        }

    @property
    def rotated_data(self):
        return rotate_data(self.tile.data, self.angle)

    @property
    def flipped_data(self):
        return flip_data(self.rotated_data, self.flip)

    @property
    def data(self):
        return ["".join(line) for line in self.flipped_data]


class Puzzle:
    solution = None

    def find_candidates(self, pos_tile, source_edge, dest_edge, completed):
        for pos_candidate in self.edge_cache[dest_edge][
            pos_tile.edges[source_edge]
        ]:
            if pos_candidate.tile_id == pos_tile.tile_id:
                continue
            if pos_candidate.tile_id in completed:
                pos_candidate = completed[pos_candidate.tile_id]
                if getattr(pos_candidate, dest_edge):
                    continue
                yield pos_candidate
            yield pos_candidate

    def build(self, pos_tile, completed=None):
        if not completed:
            completed = {}

        if len(completed) == len(self.tiles):
            return completed

        for source_edge, dest_edge in EDGE_RELATIONS.items():
            new_completed = completed.copy()
            new_completed[pos_tile.tile_id] = pos_tile
            for candidate in self.find_candidates(
                pos_tile, source_edge, dest_edge, new_completed
            ):
                setattr(candidate, dest_edge, pos_tile)
                setattr(pos_tile, source_edge, candidate)
                new_completed[candidate.tile_id] = candidate
                if ret := self.build(candidate, new_completed):
                    return ret

        return {}

    def resolve(self):
        self.solution = self.build(self.tiles[0].get_positioned())

    def __init__(self, tiles):
        self.tiles = tiles
        self.build_cache()

    def build_cache(self):
        self.edge_cache = {}
        for edge in [*EDGE_RELATIONS]:
            self.edge_cache[edge] = defaultdict(list)
            for tile in self.tiles:
                for angle, flip in VARIANTS:
                    pos_tile = tile.get_positioned(angle, flip)
                    self.edge_cache[edge][pos_tile.edges[edge]].append(
                        pos_tile
                    )

    def get_grid(self):
        displayed = set()
        grid = defaultdict(dict)

        def arrange(tile, y, x):
            if tile not in displayed:
                displayed.add(tile)
                grid[y][x] = tile
                for rel_y, rel_x, edge in zip(
                    (-1, 0, 1, 0), (0, 1, 0, -1), [*EDGE_RELATIONS]
                ):
                    if getattr(tile, edge):
                        arrange(getattr(tile, edge), y + rel_y, x + rel_x)

        arrange(list(self.solution.values())[0], 0, 0)
        return grid

    def display_grid(self):
        grid = self.get_grid()
        for y in sorted(grid):
            for x in sorted(grid[y]):
                print(grid[y][x].tile_id, end=" ")
            print()

    def display_graphic_grid(self):
        grid = self.get_grid()
        for y in sorted(grid):
            for index in range(0, 10):
                for x in sorted(grid[y]):
                    print(grid[y][x].data[index], end=" ")
                print()
            print()

    def get_image(self):
        grid = self.get_grid()
        image = []
        for y in sorted(grid):
            for index in range(1, 9):
                line = ""
                for x in sorted(grid[y]):
                    line += "".join(grid[y][x].data[index][1:9])
                image.append(line)
        return image

    def get_monster_image(self, monster):
        image = self.get_image()
        for angle, flip in VARIANTS:
            monster_count = 0
            oriented_image = flip_data(rotate_data(image, angle), flip)
            for yi, y in enumerate(oriented_image[: -len(monster) + 1]):
                for xi, x in enumerate(y[: -len(monster[0]) + 1]):
                    if self.search_monster(oriented_image, monster, yi, xi):
                        monster_count += 1
            if monster_count:
                return "\n".join(["".join(line) for line in oriented_image])

    def search_monster(self, image, monster, yi, xi):
        monster_indexes = []
        for ryi in range(0, len(monster)):
            for rxi in range(0, len(monster[0])):
                if monster[ryi][rxi] == "#":
                    if image[yi + ryi][xi + rxi] == "#":
                        monster_indexes.append((yi + ryi, xi + rxi))
                    else:
                        return False
        for yi, xi in monster_indexes:
            image[yi][xi] = "O"
        return True

    def print_solution(self):
        for tile_id, tile in self.solution.items():
            print(
                f"{tile_id} {tile.top} {tile.right} {tile.bottom} {tile.left}"
            )

    @property
    def corner_product(self):
        grid = self.get_grid()
        first_y = sorted(grid)[0]
        last_y = sorted(grid)[-1]
        first_x = sorted(grid[first_y])[0]
        last_x = sorted(grid[first_y])[-1]
        res = reduce(
            mul,
            [
                grid[y][x].tile_id
                for y, x in list(product((first_y, last_y), (first_x, last_x)))
            ],
        )
        return res


if __name__ == "__main__":
    filename = sys.argv[1]

    tiles = []
    for tile_data in [
        line.split("\n")
        for line in open(filename, "r").read().strip().split("\n\n")
    ]:
        tile_id = int(tile_data[0][5:-1])
        tiles.append(Tile(tile_id, tile_data[1:]))

    monster = [line[:-1] for line in open("monster", "r")]

    puzzle = Puzzle(tiles)
    puzzle.resolve()
    monster_image = puzzle.get_monster_image(monster)
    print(monster_image)
    print(f"Product of corners is {puzzle.corner_product}")
    res2 = sum([1 for line in monster_image for char in line if char == "#"])
    print(f"Water is {res2} rough")
