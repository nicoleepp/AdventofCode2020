import string

with open("Day 6/input.txt", "r") as f:
    group_declarations = f.read().split("\n\n")


# Part 1
total_num_answered = 0
for group_declaration in group_declarations:
    group_declaration = ''.join(group_declaration.split())
    num_answers = len(set(group_declaration))

    # print(f"The number of questions answered for group {group_declaration} is {num_answers}")
    total_num_answered += num_answers

print(f"The total number of answers for all groups is {total_num_answered}")

# Part 2
total_num_answered = 0
for group_declaration in group_declarations:
    group_declaration = (group_declaration.split())
    group_answers = [ch for ch in string.ascii_lowercase if (all(ch in ans for ans in group_declaration))]
    num_answers = len(group_answers)

    # print(f"The number of questions answered for group {group_declaration} is {num_answers}")
    total_num_answered += num_answers

print(f"The total number of answers for all groups is {total_num_answered}")
