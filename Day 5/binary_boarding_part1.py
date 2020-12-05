import math


with open("Day 5/input.txt", "r") as f:
    boarding_passes = f.read().splitlines()


def find_row(guide, start, stop):
    seat_range = math.ceil((stop-start)/2)

    # Select front half of seat ranges
    if guide[0] == 'F':
        stop -= seat_range
    elif guide[0] == 'B':
        start += seat_range

    if len(guide) == 1:
        return start

    return find_row(guide[1:], start, stop)

def find_col(guide, start, stop):
    seat_range = math.ceil((stop-start)/2)

    if guide[0] == 'L':
        stop -= seat_range
    elif guide[0] == 'R':
        start += seat_range

    if len(guide) == 1:
        return start

    return find_col(guide[1:], start, stop)

def find_seat_id(boarding_pass):
    row = find_row(boarding_pass[0:7], 0, 127)
    col = find_col(boarding_pass[7:], 0, 8)
    ID = row * 8 + col

    print(f"The seat is at row {row} and col {col}, with ID {ID}")
    return ID


highest = -1
for boarding_pass in boarding_passes:
    ID = find_seat_id(boarding_pass)
    if ID > highest:
        highest = ID

print(f"The highest seat ID is: {highest}")
