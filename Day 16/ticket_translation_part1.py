class Rule:
    def __init__(self, line):
        validity_ranges = []
        name, validity = line.split(": ")
        validity = validity.split(" or ")
        for validity_range in validity:
            first, last = validity_range.split("-")

            # Add 1 because it's an inclusive range to both endpoints
            validity_ranges.append(range(int(first), int(last) + 1))
        self.name = name
        self.validity_ranges = validity_ranges

    def __str__(self):
        s = "Rule " + self.name + ": " + str(self.validity_ranges)
        return s

    def valid_field(self, field):
        return any(field in validity_range for validity_range in self.validity_ranges)


class Ticket:
    def __init__(self, line):
        self.fields = [int(x) for x in line.split(",")]

    def invalid_fields(self, rules):
        invalid_field_count = 0
        for field in self.fields:
            if not any(rule.valid_field(field) for rule in rules):
                invalid_field_count += field
        return invalid_field_count


if __name__ == "__main__":
    with open("Day 16/input.txt", "r") as f:
        input = f.read()

    rules, my_ticket, other_tickets = input.split("\n\n")
    rules = [Rule(line) for line in rules.splitlines()]
    tickets = [Ticket(line) for line in other_tickets.splitlines()[1:]]

    invalid_value_count = sum(ticket.invalid_fields(rules) for ticket in tickets)
    print(f"The count of invalid fields found in other tickets was {invalid_value_count}")
