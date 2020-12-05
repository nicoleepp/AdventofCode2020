with open("Day 3/input.txt", "r") as f:
    map = f.read().splitlines()

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y

right_slope = 3
down_slope = 1

curr_pos = Position()
reached_bottom = False
num_trees = 0
map_width = len(map[1])

while reached_bottom is False:
    curr_pos.move(right_slope, down_slope)

    if curr_pos.y >= len(map):
        reached_bottom = True
        break

    if map[curr_pos.y][curr_pos.x % map_width] == '#':
        num_trees += 1

print(f"The number of tress encountered was: {num_trees}")
