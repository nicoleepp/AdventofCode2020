
with open("Day 2/input.txt", "r") as f:
    passwords = f.read().splitlines()

valid_count = 0
for line in passwords:
    rule, password = line.split(": ")
    occurances, letter = rule.split(" ")
    min_occurances, max_occurances = [int(x) for x in occurances.split("-")]

    actual_occurances = password.count(letter)
    if actual_occurances >= min_occurances and actual_occurances <= max_occurances:
        valid_count += 1

print(f"There are {valid_count} valid passwords.\n\n")

valid_count = 0
for line in passwords:
    rule, password = line.split(": ")
    positions, letter = rule.split(" ")
    pos_1, pos_2 = [int(x) for x in positions.split("-")]

    cond_1 = len(password) >= pos_1 and password[pos_1 - 1] == letter
    cond_2 = len(password) >= pos_2 and password[pos_2 - 1] == letter

    # ^ is xor
    if cond_1 ^ cond_2:
        print(f"Valid password {password} for rule {rule}.")
        valid_count += 1

print(f"There are {valid_count} valid passwords")
