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

    def num_adjacent_occupied(self, x, y):
        num_occupied = 0
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                if i == x and j == y:
                    continue
                if i < 0 or i >= self.num_rows:
                    continue
                if j < 0 or j >= self.num_cols:
                    continue
                if self.grid[i][j] == "#":
                    num_occupied += 1
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
                num_adjacent = self.num_adjacent_occupied(x, y)
                if self.grid[x][y] == 'L' and num_adjacent == 0:
                    new[x][y] = "#"
                    made_changes = True
                elif self.grid[x][y] == '#' and num_adjacent >= 4:
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
