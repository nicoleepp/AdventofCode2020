ACTIVE_STATE = "#"
INACTIVE_STATE = "."
NUM_CYCLES = 6


def num_active_neighbours(cubes, cube):
    x, y, z = cube
    num_active = 0

    for curr_x in (x-1, x, x+1):
        for curr_y in (y-1, y, y+1):
            for curr_z in (z-1, z, z+1):

                if curr_x == x and curr_y == y and curr_z == z:
                    continue

                state = cubes.get((curr_x, curr_y, curr_z), None)
                if state is not None and state == ACTIVE_STATE:
                    num_active += 1

    return num_active


def new_grid(cubes):
    new_cubes = {}
    for (x, y, z) in cubes:
        for curr_x in (x-1, x, x+1):
            for curr_y in (y-1, y, y+1):
                for curr_z in (z-1, z, z+1):

                    state = cubes.get((curr_x, curr_y, curr_z), None)
                    if state is None:
                        new_cubes[(curr_x, curr_y, curr_z)] = INACTIVE_STATE
                    elif state == ACTIVE_STATE:
                        new_cubes[(curr_x, curr_y, curr_z)] = ACTIVE_STATE
                    else:
                        new_cubes[(curr_x, curr_y, curr_z)] = INACTIVE_STATE
    return new_cubes


if __name__ == "__main__":
    with open("Day 17/input.txt", "r") as f:
        input = f.read().splitlines()

    cubes = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            cubes[(x, y, 0)] = input[y][x]


    for _ in range(NUM_CYCLES):
        new_cubes = new_grid(cubes)

        for cube in new_cubes:
            num_neighbours = num_active_neighbours(cubes, cube)

            if new_cubes[cube] == ACTIVE_STATE:
                if num_neighbours not in (2, 3):
                    new_cubes[cube] = INACTIVE_STATE
            else:
                if num_neighbours == 3:
                    new_cubes[cube] = ACTIVE_STATE

        cubes = new_cubes

    num_active = 0
    for cube in cubes:
        if cubes[cube] == ACTIVE_STATE:
            num_active += 1

    print(num_active)
