import re

def parse_rules(input):
    rules = {}
    i = 0
    line = input[i]
    while line != "":
        rule_num, rules_input = line.split(": ")
        rules[rule_num] = rules_input.split(" ")
        i += 1
        line = input[i]
    return rules, i


def build_regex(rules, rule_num):
    regex = "("

    for x in rules[rule_num]:
        if x.startswith("\"") or x == "|":
            regex += x.replace("\"", "")
        else:
            regex += build_regex(rules, x)

    regex += ")"
    return regex


def find_matches(input, regex):
    num_matches = 0
    for line in input:
        if re.match(regex, line) is not None:
            num_matches += 1
    return num_matches


if __name__ == "__main__":
    with open("Day 19/input.txt", "r") as f:
        input = f.read().splitlines()

    rules, i = parse_rules(input)

    pattern = build_regex(rules, "0")
    pattern += "\\b"  # Insist the whole word be matched
    regex = re.compile(pattern)

    num_matches = find_matches(input[i+1:], regex)
    print(num_matches)
