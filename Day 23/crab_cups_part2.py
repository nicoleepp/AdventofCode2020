
class LinkedList:
    def __init__(self, values, num):
        # Create list
        self.root = Node(values[0])
        prev = self.root
        for i in range(1, num):
            curr = Node(values[i])
            prev.next = curr
            prev = curr
        prev.next = self.root

        # Set max and min nodes
        max_node = self.root
        min_node = self.root
        curr = self.root
        self.fast_lookup = {curr.label: curr}

        # Set initial max and min nodes
        for i in range(1, num):
            curr = curr.next
            self.fast_lookup[curr.label] = curr

            if curr.label < min_node.label:
                min_node = curr
            if curr.label > max_node.label:
                max_node = curr

        self.max = max_node
        self.min = min_node

    def set_max_and_min(self):
        max_node = self.root
        min_node = self.root
        curr = self.root

        # Find nodes
        for _ in range(1, num_cups):
            curr = curr.next
            if curr.label < min_node.label:
                min_node = curr
            if curr.label > max_node.label:
                max_node = curr

        self.max = max_node
        self.min = min_node

    def __str__(self):
        s = ""
        curr = self.root
        for _ in range(num_cups):
            s += str(curr.label) + "->"
            curr = curr.next
        return s

    def find_node(self, value):
        return self.fast_lookup[value]


class Node:
    def __init__(self, label,):
        self.label = label
        self.next = None


def pick_up_cups(cups):
    picked_up_cups = []
    curr = cups.root
    for i in range(3):
        curr = curr.next
        if i == 2:
            cups.root.next = curr.next
            curr.next = None
        picked_up_cups.append(curr)

    if any(x.label == cups.max.label for x in picked_up_cups):
        cups.set_max_and_min()

    return picked_up_cups


def select_destination_cup(cups, picked_up_cups):
    current_label = cups.root.label
    destination_label = current_label - 1
    missing_labels = [x.label for x in picked_up_cups]

    while destination_label in missing_labels:
        destination_label -= 1

    if destination_label < 1:
        return cups.max

    # Find destination cup
    return cups.find_node(destination_label)


def place(picked_up_cups, destination_cup):
    temp_next = destination_cup.next
    destination_cup.next = picked_up_cups[0]
    picked_up_cups[len(picked_up_cups) - 1].next = temp_next

    if any(x.label > cups.max.label for x in picked_up_cups):
        cups.set_max_and_min()


def find_labels(cups):
    first_cup = cups.find_node(1)

    labels = []
    labels.append(first_cup.next.label)
    labels.append(first_cup.next.next.label)

    print(labels)

    return first_cup.next.label * first_cup.next.next.label


def parse_input(input):
    cups = [int(x) for x in input]
    for i in range(max(cups) + 1, 1000000 + 1):
        cups.append(i)

    num_cups = len(cups)

    # Convert to linkedlist
    cups = LinkedList(cups, num_cups)
    return cups, num_cups


input = "315679824"
cups, num_cups = parse_input(input)

for i in range(10000000):
    picked_up_cups = pick_up_cups(cups)
    destination_cup = select_destination_cup(cups, picked_up_cups)
    place(picked_up_cups, destination_cup)
    cups.root = cups.root.next

print("\nEnd result:")
ans = find_labels(cups)
print(ans)
