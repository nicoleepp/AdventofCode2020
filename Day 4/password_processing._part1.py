import re

with open("Day 4/input.txt", "r") as f:
    passport_data = f.read().splitlines()

# Classify input by passport
passports = []
curr_data = ""
for line in passport_data:
    if len(line) == 0:
        # End of one passport, on to the next
        passports.append(curr_data)
        curr_data = ""
    else:
        if len(curr_data) > 0:
            curr_data += " "
        curr_data += line
passports.append(curr_data)

expected_fields = [
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # "cid",  # (Country ID), We want to ignore this for now
]

num_valid = 0
for passport in passports:
    if all(field in passport for field in expected_fields):
        num_valid += 1


print(f"The number of valid passports in batch is: {num_valid}")
