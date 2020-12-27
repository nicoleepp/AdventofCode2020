def flip_tile(line):
    curr = (0, 0)

    while len(line) > 0:
        if line[0] == "e":
            curr = (curr[0] + 1, curr[1])
            line = line[1:]
        elif len(line) > 1 and line[0:2] == "se":
            curr = (curr[0], curr[1] + 1)
            line = line[2:]
        elif len(line) > 1 and line[0:2] == "sw":
            curr = (curr[0] - 1, curr[1] + 1)
            line = line[2:]
        elif line[0] == "w":
            curr = (curr[0] - 1, curr[1])
            line = line[1:]
        elif len(line) > 1 and line[0:2] == "nw":
            curr = (curr[0], curr[1] - 1)
            line = line[2:]
        elif len(line) > 1 and line[0:2] == "ne":
            curr = (curr[0] + 1, curr[1] - 1)
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


tiles = {(0, 0): "white"}

with open("Day 24/input.txt", "r") as f:
    instructions = f.read().splitlines()

for line in instructions:
    flip_tile(line)

print(count_black_tiles(tiles))
