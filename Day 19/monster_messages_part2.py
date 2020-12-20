def parse_rules(input):
    rules = {}
    i = 0
    line = input[i]
    while line != "":
        rule_num, rules_input = line.split(": ")
        rules_input = rules_input.split(" | ")
        rules_input = [rule.split(" ") for rule in rules_input]
        rules[rule_num] = rules_input
        i += 1
        line = input[i]
    return rules, i


def matches(msg, given_rules):
    if len(msg) == 0:
        if len(given_rules) == 0:
            return True
        else:
            return False
    if len(given_rules) == 0:
        return False

    current_rule = rules[given_rules[0]]
    if len(current_rule) == 1 and "\"" in current_rule[0][0]:
        if msg[0] == current_rule[0][0].replace("\"", ""):
            # Check rest of the msg
            return matches(msg[1:], given_rules[1:])
        else:
            return False
    else:
        return any(matches(msg, rules + given_rules[1:]) for rules in current_rule)


if __name__ == "__main__":
    with open("Day 19/input.txt", "r") as f:
        input = f.read().splitlines()

    rules, i = parse_rules(input)
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

    num_matches = 0
    for line in input[i+1:]:
        if matches(line, ["0"]):
            num_matches += 1
    print(num_matches)
