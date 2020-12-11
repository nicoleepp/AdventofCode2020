import copy

with open("Day 11/input.txt", "r") as f:
    input = f.read().splitlines()

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[1])

    def __str__(self):
        s = ""
        for row in self.grid:
            for space in row:
                s += space
            s += "\n"
        return s

    def num_occupied_by_direction(self, x, y, increment_x, increment_y):
        curr_x = increment_x
        curr_y = increment_y
        num_occupied = 0
        found_visible = False

        while not found_visible:
            i = x + curr_x
            j = y + curr_y

            if i < 0 or i >= self.num_rows:
                break
            if j < 0 or j >= self.num_cols:
                break

            if self.grid[i][j] == "#":
                num_occupied += 1
                found_visible = True
            elif self.grid[i][j] == "L":
                found_visible = True

            curr_x += increment_x
            curr_y += increment_y
        return num_occupied

    def num_visibly_occupied(self, x, y):
        num_occupied = 0
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for inc_x, inc_y in directions:
            num_occupied +=  self.num_occupied_by_direction(x, y, inc_x, inc_y)
        return num_occupied

    def total_occupied(self):
        num_occupied = 0
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if self.grid[x][y] == '#':
                    num_occupied += 1
        return num_occupied

    def apply_rules(self):
        new = copy.deepcopy(self.grid)
        made_changes = False

        for x in range(self.num_rows):
            for y in range(self.num_cols):
                num_visibly_occupied = self.num_visibly_occupied(x, y)
                if self.grid[x][y] == 'L' and num_visibly_occupied == 0:
                    new[x][y] = "#"
                    made_changes = True
                elif self.grid[x][y] == '#' and num_visibly_occupied >= 5:
                    new[x][y] = "L"
                    made_changes = True
        self.grid = new
        return made_changes



spaces = [[space for space in line] for line in input]
grid = Grid(spaces)

made_changes = True
while made_changes:
    made_changes = grid.apply_rules()

num_occupied = grid.total_occupied()
print(f"Once people stop moving around, there are {num_occupied} occupied seats")
