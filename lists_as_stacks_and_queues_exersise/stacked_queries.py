
n = int(input())
stack_numbers = []
for num in range(n):
    command = input()
    if command.startswith('1 '):
        add_number = command.split()
        stack_numbers.append(int(add_number[1]))
    elif command == '2':
        if stack_numbers:
            stack_numbers.pop()
    elif command == '3':
        if stack_numbers:
            print(max(stack_numbers))
    elif command == '4':
        if stack_numbers:
            print(min(stack_numbers))

stack_numbers.reverse()
print(*stack_numbers, sep=', ')