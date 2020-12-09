with open("Day 9/input.txt", "r") as f:
    input = [int(x) for x in f.read().splitlines()]

PREAMBLE_LEN = 25

def valid_sum(value, options):
    options_len = len(options)
    for i in range(options_len):
        for j in range(i+1, options_len):
            if options[i] + options[j] == value:
                print(f"{value} is made from summing {options[i]} and {options[j]}")
                return True
    return False

def find_first_invalid_num(input):
    curr_pos = 0
    for value in input[PREAMBLE_LEN:]:
        options = input[curr_pos:curr_pos+PREAMBLE_LEN]

        if not valid_sum(value, options):
            print(f"No two values from {options} sum up to {value}")
            return value

        curr_pos += 1

# Part 1
find_first_invalid_num(input)

# Part 2
def find_encryption_weakness(input, invalid_num):
    input_len = len(input)

    for i in range(input_len):
        curr_sum = input[i]
        for j in range(i+1, input_len):
            curr_sum += input[j]

            if curr_sum == invalid_num:
                sum_components = input[i:j+1]
                print(f"{invalid_num} can be made from summing {sum_components}")
                return min(sum_components) + max(sum_components)

            elif curr_sum > invalid_num:
                break


invalid_num = find_first_invalid_num(input)
encryption_weakness = find_encryption_weakness(input, invalid_num)
print(f"The encryption weakness is {encryption_weakness}")
