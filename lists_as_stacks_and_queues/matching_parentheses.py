expression = input()
brackets = []

for i in range(len(expression)):
    if expression[i] == '(':
        brackets.append(i)
    elif expression[i] == ')':
        print(expression[brackets.pop():i + 1])