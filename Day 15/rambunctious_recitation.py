with open("Day 15/input.txt", "r") as f:
    numbers = [int(x) for x in f.read().split(",")]


def number_spoken(numbers, iterations):
    spoken = {}

    i = 1
    for number in numbers:
        spoken[number] = i
        i += 1

    curr_num = 0
    for i in range(i, iterations):
        if curr_num not in spoken:
            spoken[curr_num] = i
            curr_num = 0
        else:
            prev = spoken[curr_num]
            spoken[curr_num] = i
            curr_num = i - prev
    return curr_num

ans = number_spoken(numbers, 2020)
print(f"The number after 2020 iterations is {ans}")

# Part 2
ans = number_spoken(numbers, 30000000)
print(f"The number after 30000000 iterations is {ans}")
