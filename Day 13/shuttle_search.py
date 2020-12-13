with open("Day 13/input.txt", "r") as f:
    input = f.read().splitlines()

# Part 1
earliest_timestamp = int(input[0])
bus_ids = [int(x) for x in input[1].split(",") if x != "x"]

waiting_time = 0
departed = False
while departed != True:
    curr_timestamp = earliest_timestamp + waiting_time

    for bus_id in bus_ids:
        if curr_timestamp % bus_id == 0:
            departed = True
            print(f"The earliest bus you could take is bus ID {bus_id} after waiting {waiting_time} minutes")
            print(f"Multiplied together that's {bus_id * waiting_time}")
            break

    waiting_time += 1


# Part 2
bus_ids = [x for x in input[1].split(",")]
positions = [i for i in range(len(bus_ids)) if bus_ids[i] != "x"]

# Remove unneeded "x" bus ids
bus_ids = [int(x) for x in bus_ids if x != "x"]

# Calculate modulos for chinee remainder theorem
modulos = [bus_ids[i] - positions[i] for i in range(len(bus_ids))]

# The earliest possible timestamp is congruent to (bus_id - position) (mod bus_id)
# for all bus ids and their positions
# The implementation is from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(bus_ids, modulos):
    sum = 0

    product = 1
    for bus_id in bus_ids:
        product *= bus_id

    for bus_id, modulo in zip(bus_ids, modulos):
        p = product // bus_id
        sum += modulo * mul_inv(p, bus_id) * p

    return sum % product

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

ans = chinese_remainder(bus_ids, modulos)
print(f"The answer for part 2 is {ans}")
