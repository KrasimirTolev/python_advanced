from collections import deque

water = int(input())
people = deque()
liters_list = []
while True:
    name = input()
    if name == 'Start':
        break
    else:
        people.append(name)

while True:
    liters = input()
    if liters == 'End':
        break
    elif liters.startswith('refill'):
        liters_list = liters.split(' ')
        water += int(liters_list[1])
    else:
        liters = int(liters)
        if liters <= water:
            water -= liters
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')

print(f"{water} liters left")
