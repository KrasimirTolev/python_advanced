from collections import deque

robot = deque([[[_[0], int(_[1])]for _ in x.split('-')] for x in input().split(';')])
time = [int(i) for i in input().split(':')]
products = deque()
print(robot)
while True:
    product = input()
    if product == 'End':
        break
    else:
        products.append(product)


