def get_borders(tile):
    borders = [tile[0], tile[len(tile)-1]]

    left_border = ""
    right_border = ""
    for line in tile:
        left_border += line[0]
        right_border += line[len(line)-1]

    borders.append(left_border)
    borders.append(right_border)
    return borders


class Tile:
    def __init__(self, tile_input):
        tile = tile_input.splitlines()
        tile_id = int(tile[0].replace("Tile ", "").replace(":", ""))
        self.id = tile_id
        self.value = tile[1:]
        self.borders = get_borders(self.value)

    def __str__(self):
        s = "Tile ID " + str(self.id) + ": \n"
        for line in self.value:
            s +=  line + "\n"
        s += "\n"
        return s


def matches_border(a, b):
    for border_a in a.borders:
        for border_b in b.borders:
            if border_a == border_b:
                return True
            elif border_a == border_b[::-1]:
                return True
    return False


def find_corners(tiles):
    corners = []

    for i in range(len(tiles)):
        num_matched = 0

        for j in range(len(tiles)):
            if i == j:
                continue
            elif matches_border(tiles[i], tiles[j]):
                num_matched += 1

        if num_matched == 2:
            corners.append(tiles[i])

    return corners


def multiply_corner_tiles(tiles):
    corners = find_corners(tiles)

    result = 1
    for corner in corners:
        result *= corner.id
    return result


with open("Day 20/input.txt", "r") as f:
    input = f.read().split("\n\n")

tiles = [Tile(tile) for tile in input]
corners = find_corners(tiles)
ans = multiply_corner_tiles(tiles)
print(ans)
