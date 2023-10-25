from collections import deque

kids = deque(input().split(' '))
tosses = int(input())

while True:
    if len(kids) == 1:
        last_kid = kids.popleft()
        print(f'Last is {last_kid}')
        break
    for toss in range(tosses):
        kid = kids.popleft()
        if toss + 1 == tosses:
            print(f'Removed {kid}')
        else:
            kids.append(kid)

