with open("Day 3/input.txt", "r") as f:
    map = f.read().splitlines()

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y


class Slope:
    def __init__(self, right, down):
        self.right = right
        self.down = down

def calculate_num_tress(map, slope):
    curr_pos = Position()
    reached_bottom = False
    num_trees = 0
    map_width = len(map[1])

    while reached_bottom is False:
        curr_pos.move(slope.right, slope.down)

        if curr_pos.y >= len(map):
            reached_bottom = True
            break

        if map[curr_pos.y][curr_pos.x % map_width] == '#':
            num_trees += 1

    print(f"The number of tress encountered for slope Right {slope.right} and Down {slope.down} was: {num_trees}")

    return num_trees


slopes = [
    Slope(1, 1),
    Slope(3, 1),
    Slope(5, 1),
    Slope(7, 1),
    Slope(1, 2),
]

total_result = 1
for slope in slopes:
    curr_result = calculate_num_tress(map, slope)
    total_result *= curr_result

print(f"The total result is {total_result}")
