with open("Day 10/input.txt", "r") as f:
    adapters = sorted([int(x) for x in f.read().splitlines()])

# Append built in adapter
adapters.append(adapters[-1] + 3)

# Part 1
voltage_differences = []
prev = 0
for adapter in adapters:
    curr = adapter
    diff = curr - prev
    voltage_differences.append(diff)
    prev = curr

ans = voltage_differences.count(1) * voltage_differences.count(3)

print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is {ans}")


# Part 2
adapters.insert(0, 0)

# Cache previously calculated number of arrangements
num_combinations = {}

def count_combinations(i, adapters, num_combinations):
    if i == 0 or i == 1:
        num_combinations[i] = 1
    else:
        curr_count = num_combinations[i-1]

        if adapters[i] - adapters[i-2] <= 3:
            curr_count += num_combinations[i-2]

        if i >= 3 and adapters[i] - adapters[i-3] <= 3:
             curr_count += num_combinations[i-3]

        num_combinations[i] = curr_count


for x in range(len(adapters)):
    count_combinations(x, adapters, num_combinations)

print(f"There are {num_combinations[len(adapters)-1]} distint arrangmenets")
