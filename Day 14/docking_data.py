import re

with open("Day 14/input.txt", "r") as f:
    input = f.read().splitlines()


def base2encode(num):
    result = ""
    while num != 0:
        q = num // 2
        remainder = num % 2
        result = str(remainder) + result
        num = q
    pad = 36 - len(result)
    for _ in range(pad):
        result = "0" + result
    return result

def process_input(input):
    mask = input[0].split(" = ")[1]

    memory = {}
    for line in input[1:]:
        identifier, value = line.split(" = ")

        if identifier == "mask":
            mask = value
            continue

        memory_location = re.match(r"mem\[(\d*)\]", identifier)
        if memory_location:
            items = memory_location.groups()
            memory_location = int(items[0])

        decimal_value = base2encode(int(value))

        new_value = ""
        for i in range(len(mask)):
            if mask[i] == "1" or mask[i] == "0":
                new_value += mask[i]
            else:
                new_value += decimal_value[i]

        # Convert back from a decimal string
        new_value = int(new_value, 2)

        # Store in memory
        memory[memory_location] = new_value

    return memory

def sum_memory(memory):
    return sum(item for item in memory.values())


memory = process_input(input)
ans = sum_memory(memory)
print(f"The sum of the values stored in memory is {ans}")


# Part 2
def split_values(value):
    curr = ""
    for i in range(len(value)):
        if value[i] == "X":
            values = []
            if i == len(value) - 1:
                values.append(curr + "0")
                values.append(curr + "1")
            else:
                possibilities = split_values(value[i+1:])
                for possibility in possibilities:
                    values.append(curr + "0" + possibility)
                    values.append(curr + "1" + possibility)

            return values
        else:
            curr += value[i]
    return [curr]


def new_values(mask, decimal_value):
    value = ""
    for i in range(len(mask)):
        if mask[i] == "1":
            value += mask[i]
        elif mask[i] == "0":
            value += decimal_value[i]
        else:
            value += "X"

    return [int(x, 2) for x in split_values(value)]


def process_input_part2(input):
    mask = input[0].split(" = ")[1]

    memory = {}
    for line in input[1:]:
        identifier, value = line.split(" = ")

        if identifier == "mask":
            mask = value
            continue

        memory_location = re.match(r"mem\[(\d*)\]", identifier)
        if memory_location:
            items = memory_location.groups()
            memory_location = int(items[0])

        decimal_value = base2encode(int(memory_location))
        memory_locations = new_values(mask, decimal_value)

        # Store in memory
        for location in memory_locations:
            memory[location] = int(value)

    return memory

print(f"\nPart 2:")
memory = process_input_part2(input)
ans = sum_memory(memory)
print(f"The sum of the values stored in memory is {ans}")
