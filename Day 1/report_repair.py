
TOTAL_SUM = 2020

f = open("Day 1/input.txt", "r")
expenses = [int(x) for x in f.read().splitlines()]
f.close()

for expense in expenses:
    diff = TOTAL_SUM - expense
    if diff in expenses:
        print("Found ", diff, " and ", expense, " that sum up to ", TOTAL_SUM)
        print("Together they multiply to: ", diff * expense)
        break


found = False
for i in range(0, len(expenses) - 1):
    first_expense = expenses[i]
    remaining_diff = TOTAL_SUM - first_expense

    for j in range(i + 1, len(expenses) - 1):
        second_expense = expenses[j]
        third_expense = remaining_diff - second_expense
        if third_expense in expenses:
            print("Found ", first_expense, ", ", second_expense, ", and ", third_expense, " that sum up to ", TOTAL_SUM)
            print("Together they multiply to: ", first_expense * second_expense * third_expense)
            found = True
            break
    if found:
        break
