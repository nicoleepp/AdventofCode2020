import copy


def e(curr):
    return (curr[0] + 1, curr[1])

def se(curr):
    return (curr[0], curr[1] + 1)

def sw(curr):
    return (curr[0] - 1, curr[1] + 1)

def w(curr):
    return (curr[0] - 1, curr[1])

def nw(curr):
    return (curr[0], curr[1] - 1)

def ne(curr):
    return (curr[0] + 1, curr[1] - 1)


directions = {"e": e, "se": se, "sw": sw, "w": w, "nw": nw, "ne": ne}


def flip_tile(line):
    curr = (0, 0)

    while len(line) > 0:
        if line[0] == "e":
            curr = e(curr)
            line = line[1:]
        elif len(line) > 1 and line[0:2] == "se":
            curr = se(curr)
            line = line[2:]
        elif len(line) > 1 and line[0:2] == "sw":
            curr = sw(curr)
            line = line[2:]
        elif line[0] == "w":
            curr = w(curr)
            line = line[1:]
        elif len(line) > 1 and line[0:2] == "nw":
            curr = nw(curr)
            line = line[2:]
        elif len(line) > 1 and line[0:2] == "ne":
            curr = ne(curr)
            line = line[2:]

    if curr not in tiles or tiles[curr] == "white":
        tiles[curr] = "black"
    else:
        tiles[curr] = "white"


def count_black_tiles(tiles):
    black_tiles_count = 0
    for colour in tiles.values():
        if colour == "black":
            black_tiles_count += 1
    return black_tiles_count


def num_adjacent(colour, tile, tiles):
    num = 0

    for get_adjacent in directions.values():
        neighbour = get_adjacent(tile)
        if neighbour in tiles and tiles[neighbour] == colour:
            num += 1
    return num


def flip_daily_tiles(tiles):
    new_tiles = copy.deepcopy(tiles)

    for tile in tiles:
        for get_adjacent in directions.values():
            neighbour = get_adjacent(tile)
            if neighbour not in tiles:
                new_tiles[neighbour] = "white"

    for tile in new_tiles:
        num_adjacent_black_tiles = num_adjacent("black", tile, tiles)

        if tile in tiles and tiles[tile] == "black" and (num_adjacent_black_tiles == 0 or num_adjacent_black_tiles > 2):
            new_tiles[tile] = "white"

        elif (tile not in tiles or tiles[tile] == "white") and num_adjacent_black_tiles == 2:
            new_tiles[tile] = "black"

    return new_tiles



tiles = {(0, 0): "white"}

with open("Day 24/input.txt", "r") as f:
    instructions = f.read().splitlines()

for line in instructions:
    flip_tile(line)

for day in range(1, 100 + 1):
    tiles = flip_daily_tiles(tiles)
    num_black_tiles = count_black_tiles(tiles)

    if day == 100:
        print(f"Day {day}: {num_black_tiles}")
