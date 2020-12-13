with open("Day 12/input.txt", "r") as f:
    navigation_instructions = f.read().splitlines()


class Ship:
    def __init__(self):
        self.rotation_degrees = 0
        self.east_west_pos = 0
        self.north_south_pos = 0

    def __str__(self):
        s = "Degrees = " + str(self.rotation_degrees)
        s += "\nEast West position = " + str(self.east_west_pos)
        s += "\nSouth Noth position = " + str(self.north_south_pos) + "\n"
        return s

    def direction(self):
        if self.rotation_degrees > 315 or self.rotation_degrees <= 45:
            return "E"
        elif self.rotation_degrees > 45 and self.rotation_degrees <= 135:
            return "S"
        elif self.rotation_degrees > 135 and self.rotation_degrees <= 225:
            return "W"
        elif self.rotation_degrees > 225 and self.rotation_degrees <= 315:
            return "N"

    def manhattan_distance(self):
        return abs(self.east_west_pos) + abs(self.north_south_pos)

    def move_forward(self, value):
        if self.direction() == "E":
            self.move_east(value)
        elif self.direction() == "W":
            self.move_west(value)
        elif self.direction() == "N":
            self.move_north(value)
        elif self.direction() == "S":
            self.move_south(value)

    def move_north(self, value):
        self.north_south_pos += value

    def move_south(self, value):
        self.north_south_pos -= value

    def move_east(self, value):
        self.east_west_pos += value

    def move_west(self, value):
        self.east_west_pos -= value

    def rotate_right(self, degrees):
        self.rotation_degrees = (self.rotation_degrees + degrees) % 360

    def rotate_left(self, degrees):
        self.rotation_degrees = (self.rotation_degrees - degrees) % 360

    def move(self, instructions):
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
            elif direction == "L":
                self.rotate_left(value)
            elif direction == "R":
                self.rotate_right(value)
            elif direction == "F":
                self.move_forward(value)


ship = Ship()
ship.move(navigation_instructions)
manhattan_distance = ship.manhattan_distance()
print(f"The manhattan distance of the ship from its starting position is {manhattan_distance}")
