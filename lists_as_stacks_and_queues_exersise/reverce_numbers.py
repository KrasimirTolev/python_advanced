numbers = input().split()
reversed_numbers = []

for index in range(len(numbers)):
    reversed_numbers.append(numbers.pop())

print(' '.join(reversed_numbers))
