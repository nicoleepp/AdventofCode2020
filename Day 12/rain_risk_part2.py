with open("Day 12/input.txt", "r") as f:
    navigation_instructions = f.read().splitlines()


class Ship:
    def __init__(self):
        self.east_west_pos = 0
        self.north_south_pos = 0
        self.waypoint = Waypoint()

    def __str__(self):
        s = "\nEast West position = " + str(self.east_west_pos)
        s += "\nSouth Noth position = " + str(self.north_south_pos) + "\n"
        s += "and it's waypoint is at " + str(self.waypoint) + "\n"
        return s

    def manhattan_distance(self):
        return abs(self.east_west_pos) + abs(self.north_south_pos)

    def move_north(self, value):
        self.north_south_pos += value

    def move_south(self, value):
        self.north_south_pos -= value

    def move_east(self, value):
        self.east_west_pos += value

    def move_west(self, value):
        self.east_west_pos -= value

    def move_forward(self, value):
        instructions = self.waypoint.relative_position()
        for _ in range(value):
            for instruction in instructions:
                direction = instruction[0]
                value = int(instruction[1:])

                if direction == "N":
                    self.move_north(value)
                elif direction == "S":
                    self.move_south(value)
                if direction == "E":
                    self.move_east(value)
                elif direction == "W":
                    self.move_west(value)

    def move(self, instructions):
        for instruction in instructions:
            direction = instruction[0]
            value = int(instruction[1:])

            if direction == "N":
                self.waypoint.move_north(value)
            elif direction == "S":
                self.waypoint.move_south(value)
            if direction == "E":
                self.waypoint.move_east(value)
            elif direction == "W":
                self.waypoint.move_west(value)
            elif direction == "L":
                self.waypoint.rotate_left(value)
            elif direction == "R":
                self.waypoint.rotate_right(value)
            elif direction == "F":
                self.move_forward(value)
            # print(f"After executing {instruction}, the ship's position is {self}")


class Waypoint:
    def __init__(self):
        self.east_west_pos = 10
        self.north_south_pos = 1

    def __str__(self):
        s = "East West position = " + str(self.east_west_pos)
        s += " and South Noth position = " + str(self.north_south_pos) + "\n"
        return s

    def relative_position(self):
        instructions = []
        if self.east_west_pos >= 0:
            instructions.append("E" + str(self.east_west_pos))
        else:
            instructions.append("W" + str(abs(self.east_west_pos)))
        if self.north_south_pos >= 0:
            instructions.append("N" + str(self.north_south_pos))
        else:
            instructions.append("S" + str(abs(self.north_south_pos)))
        return instructions

    def move_north(self, value):
        self.north_south_pos += value

    def move_south(self, value):
        self.north_south_pos -= value

    def move_east(self, value):
        self.east_west_pos += value

    def move_west(self, value):
        self.east_west_pos -= value

    def turn_right(self):
        original_east_west = self.east_west_pos
        original_noth_south = self.north_south_pos
        self.north_south_pos = -original_east_west
        self.east_west_pos = original_noth_south

    def turn_left(self):
        original_east_west = self.east_west_pos
        original_noth_south = self.north_south_pos
        self.north_south_pos = original_east_west
        self.east_west_pos = -original_noth_south

    def rotate_right(self, degrees):
        for i in range(int(degrees/90)):
            self.turn_right()

    def rotate_left(self, degrees):
        for i in range(int(degrees/90)):
            self.turn_left()


ship = Ship()
ship.move(navigation_instructions)
manhattan_distance = ship.manhattan_distance()
print(f"The manhattan distance of the ship from its starting position is {manhattan_distance}")
