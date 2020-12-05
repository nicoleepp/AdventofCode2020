import math

MAX_ROW = 127
MAX_COL = 8
MAX_SEAT_ID = MAX_ROW * MAX_COL + MAX_COL

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

    # Select front half of seat ranges
    if guide[0] == 'L':
        stop -= seat_range
    elif guide[0] == 'R':
        start += seat_range

    if len(guide) == 1:
        return start

    return find_col(guide[1:], start, stop)

def find_seat_id(boarding_pass):
    row = find_row(boarding_pass[0:7], 0, MAX_ROW)
    col = find_col(boarding_pass[7:], 0, MAX_COL)
    ID = row * 8 + col
    return ID


boarded_seats = [find_seat_id(boarding_pass) for boarding_pass in boarding_passes]

for seat in range(MAX_SEAT_ID):
    if seat not in boarded_seats:
        if seat > 0 and seat < MAX_SEAT_ID:
            if (seat - 1) in boarded_seats and (seat + 1) in boarded_seats:
                print(f"Your seat is the one with ID {seat}")
                break
