MAX_VALUE = 20201227
SUBJECT_NUM = 7


def transform_subject_num(subject_num, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_num
        value = value % MAX_VALUE
    return value


def calculate_loop_size(subject_num, key):
    found = False
    loop_size = 1

    value = 1
    while not found:
        value *= subject_num
        value = value % MAX_VALUE
        if value == key:
            return loop_size
        loop_size += 1


with open("Day 25/input.txt", "r") as f:
    card_key, door_key = (int(x) for x in f.read().splitlines())

door_loop_size = calculate_loop_size(SUBJECT_NUM, door_key)
encryption_key = transform_subject_num(card_key, door_loop_size)
print(encryption_key)
