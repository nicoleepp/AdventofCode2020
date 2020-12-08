import copy

with open("Day 8/input.txt", "r") as f:
    input = f.read().splitlines()


class InstructionLine:
    def __init__(self, line):
        instruction, value = line.split(" ")
        self.instruction = instruction
        self.value = int(value)
        self.executed = False

lines = [InstructionLine(line) for line in input]

def test_instructions(lines):
    acc = 0
    curr_line = 0

    while True:
        if curr_line >= len(lines):
            print(f"Program terminates! acc is {acc}\n")
            return True

        line = lines[curr_line]
        # print(f"Executing {line.instruction} {line.value}. acc is {acc}")

        if line.executed == True:
            print(f"Already executed {line.instruction} {line.value}. acc is {acc}\n")
            return False

        if line.instruction == "nop":
            curr_line += 1
        elif line.instruction == "acc":
            acc += line.value
            curr_line += 1
        elif line.instruction == "jmp":
            curr_line += line.value
        line.executed = True
    return False

# Part 1
curr_lines = copy.deepcopy(lines)
test_instructions(curr_lines)

# Part 2
def change_instruction(line):
    if line.instruction == "nop":
        line.instruction = "jmp"
    elif line.instruction == "jmp":
        line.instruction = "nop"

for i in range(len(lines)):
    curr_lines = copy.deepcopy(lines)
    line = curr_lines[i]

    change_instruction(line)

    if test_instructions(curr_lines) is True:
        break
