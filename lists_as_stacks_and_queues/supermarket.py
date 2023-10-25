from collections import deque

clients = deque()

while True:
    name = input()
    if name == 'End':
        break
    elif name == 'Paid':
        while True:
            if len(clients) == 0:
                break
            else:
                print(clients.popleft())
    else:
        clients.append(name)

print(f"{len(clients)} people remaining.")