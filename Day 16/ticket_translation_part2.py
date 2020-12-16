class Rules:
    def __init__(self, rules):
        self.rules = [Rule(line) for line in rules.splitlines()]

    def __str__(self):
        s = "Rules: \n"
        for rule in self.rules:
            s += str(rule) + "\n"
        return s

    def calculate_positions(self, valid_tickets):
        num_fields = len(valid_tickets[1].fields)

        # Determine possible rules that apply to each field
        possibile_fields = {}
        for rule in self.rules:
            possibile_fields[rule] = []

        for i in range(num_fields):
            for rule in self.rules:
                if all(rule.valid_field(ticket.fields[i]) for ticket in valid_tickets):
                    possibile_fields[rule].append(i)

        # Figure out which rule applies to which field
        total_rules = len(self.rules)
        num_found = 0
        while num_found < total_rules:
            for rule in self.rules:
                if rule.field_position == None:
                    if len(possibile_fields[rule]) == 1:
                        field_pos = possibile_fields[rule][0]
                        rule.field_position = field_pos
                        num_found += 1

                        # Remove field from other rule possibilities
                        for value in possibile_fields.values():
                            if field_pos in value:
                                value.remove(field_pos)


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
        self.field_position = None

    def __str__(self):
        s = "Rule " + self.name + ": " + str(self.validity_ranges)
        if self.field_position is not None:
            s +=  ", located at " + str(self.field_position)
        return s

    def valid_field(self, field):
        return any(field in validity_range for validity_range in self.validity_ranges)


class Ticket:
    def __init__(self, line):
        self.fields = [int(x) for x in line.split(",")]

    def valid(self, rules):
        valid = True
        for field in self.fields:
            if not any(rule.valid_field(field) for rule in rules):
                valid = False
        return valid

    def multiply_departure_fileds(self, rules):
        result = 1
        for rule in rules:
            if rule.name.startswith("departure"):
                result *= self.fields[rule.field_position]
        return result


if __name__ == "__main__":
    with open("Day 16/input.txt", "r") as f:
        input = f.read()

    rules, my_ticket, other_tickets = input.split("\n\n")
    rules = Rules(rules)
    tickets = [Ticket(line) for line in other_tickets.splitlines()[1:]]
    valid_tickets = [ticket for ticket in tickets if ticket.valid(rules.rules)]

    rules.calculate_positions(valid_tickets)

    my_ticket = Ticket(my_ticket.splitlines()[1])
    ans = my_ticket.multiply_departure_fileds(rules.rules)

    print(f"The departure fields multiplied on my ticket: {ans}")
