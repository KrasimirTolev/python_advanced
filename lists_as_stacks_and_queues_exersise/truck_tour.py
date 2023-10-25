from collections import deque


qty_gas_station = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

tank = 0
index = 0
qty_gas_station_copy = qty_gas_station.copy()

while qty_gas_station_copy:
    petrol, distance = qty_gas_station_copy.popleft()
    tank += petrol

    if tank >= distance:
        tank -= distance
    else:
        qty_gas_station.rotate(-1)
        qty_gas_station_copy = qty_gas_station.copy()
        index += 1
        tank = 0


print(index)


