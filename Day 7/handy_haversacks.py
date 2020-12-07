import re

with open("Day 7/input.txt", "r") as f:
    input = f.read().splitlines()


rules = {}
for line in input:
    label, containing_rules = line.split("contain")
    label = label.replace(" bags ", "")
    containing_rules = containing_rules.split(',')

    rules[label] = {}
    for rule in containing_rules:

        match = re.match(r"\s(\d{1})\s([a-z]+)\s([a-z]+)\sbag", rule)
        if match:
            items = match.groups()
            number = int(items[0])
            rule_label = ' '.join(items[1:])

            rules[label][rule_label] = number

# Part 1
def can_contain(outer_bag, inner_bag):
    outer_bag_contents = rules[outer_bag]
    if inner_bag in outer_bag_contents.keys():
        return True

    return any(can_contain(bag, inner_bag) for bag in outer_bag_contents)


can_contain_shiny_gold_bag_count = 0
for label in rules:
    if can_contain(label, "shiny gold"):
        can_contain_shiny_gold_bag_count += 1


print(f"{can_contain_shiny_gold_bag_count} bags can contain a shiny gold bag\n")


# Part 2
def count_bags(rules, label):
    bag_contents = rules[label]
    if len(bag_contents) == 0:
        return 0

    counts = [count + count * count_bags(rules, sub_label) for (sub_label, count) in bag_contents.items()]
    return sum(counts)

num_bags = 0
num_bags = count_bags(rules, "shiny gold")
print(f"A single shiny gold bag must contain {num_bags} other bags.\n")
