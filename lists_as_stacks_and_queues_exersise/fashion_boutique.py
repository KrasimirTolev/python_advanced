from collections import deque

box_clothes = deque(map(int, input().split()))
capacity_rack = int(input())
current_rack = capacity_rack
qty_racks = 1

while box_clothes:
    cloth = box_clothes.pop()
    if current_rack >= cloth:
        current_rack -= cloth
    else:
        box_clothes.append(cloth)
        current_rack = capacity_rack
        qty_racks += 1

print(qty_racks)