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

def isvalid(passport, expected_fields):
    if not all(field in passport for field in expected_fields):
        return False

    if re.search(r"byr:((19[2-9]\d)|(200[0-2]))", passport) is None:
        return False

    if re.search(r"iyr:20((1\d)|(20))", passport) is None:
        return False

    if re.search(r"eyr:20((2\d)|(30))", passport) is None:
        return False

    if re.search(r"hgt:((1(([5-8]\d)|(9[0-3]))cm)|(((59)|(6\d)|(7[0-6]))in))", passport) is None:
        return False

    if re.search(r"hcl:#(\d|[a-f]){6}\b", passport) is None:
        return False

    if re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", passport) is None:
        # print(f"Did not match ecl for passport {passport}")
        return False

    if re.search(r"pid:((\d){9})\b", passport) is None:
        # print(f"Did not match pid for passport {passport}")
        return False

    return True

num_valid = 0
for passport in passports:
    if isvalid(passport, expected_fields):
        num_valid += 1


print(f"The number of valid passports in batch is: {num_valid}")
