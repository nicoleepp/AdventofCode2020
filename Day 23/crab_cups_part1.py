def pick_up_cups(current_cup, cups):
    picked_up_cups = []
    for _ in range(3):
        cup = cups.pop((current_cup + 1))
        picked_up_cups.append(cup)
    return current_cup, picked_up_cups


def select_destination_cup(current_label, cups):
    min_value = min(cups)

    destination_label = current_label -1
    while destination_label not in cups:
        destination_label -= 1
        if destination_label < min_value:
            destination_label = max(cups)
    return cups.index(destination_label)


def place_cups(picked_up_cups, cups, curr_cup, destination_cup):
    for i in range(len(picked_up_cups)):
        cups.insert(destination_cup + 1 + i, picked_up_cups[i])


def find_labels(cups):
    label = ""
    first_index = cups.index(1)

    cups = cups[first_index+1:] + cups[:first_index]
    for cup in cups:
        label += str(cup)
    return label


input = "315679824"

cups = [int(x) for x in input]
num_cups = len(input)

current_cup = 0

for i in range(100):
    current_cup, picked_up_cups = pick_up_cups(current_cup, cups)

    current_label = cups[current_cup]
    destination_cup = select_destination_cup(current_label, cups)
    place_cups(picked_up_cups, cups, current_cup, destination_cup)

    cups = cups[1:] + [cups[0]]

labels = find_labels(cups)
print(labels)
