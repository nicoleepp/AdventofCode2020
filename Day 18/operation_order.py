def evaluate_expression(expression):
    new_expression = ""
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch == "(":
            sub_expression, sub_i = evaluate_expression(expression[i+1:])
            new_expression += str(sub_expression)
            new_expression = str(eval(new_expression))
            i += sub_i + 2
        elif ch == ")":
            return eval(new_expression), i
        elif ch == "+" or ch == "*":
            new_expression += ch
            i += 1
        elif ch != " ":
            new_expression += ch
            new_expression = str(eval(new_expression))
            i += 1
        else:
            i+=1
    return eval(new_expression), i


if __name__  == "__main__":
    with open("Day 18/input.txt", "r") as f:
        input = f.read().splitlines()

        sum_values = 0
        for line in input:
            value, index = evaluate_expression(line)
            sum_values += value
        print(sum_values)
