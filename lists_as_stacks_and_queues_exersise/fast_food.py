from collections import deque

food_qty = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

for order in orders.copy():
    if food_qty >= order:
        orders.popleft()
        food_qty -= order
    else:
        break

if len(orders) > 0:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print('Orders complete')