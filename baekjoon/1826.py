import heapq
import sys

input = sys.stdin.readline
n = int(input())
fuel_station = []
for _ in range(n):
    heapq.heappush(fuel_station, tuple(map(int, input().split())))

final_destination, current_fuel = map(int, input().split())


def g_func(fuel_station: list, final_destination: int, current_fuel: int):
    count = 0
    candidate_station = []

    while current_fuel < final_destination:
        while fuel_station and fuel_station[0][0] <= current_fuel:
            next_destination, fuel = heapq.heappop(fuel_station)
            heapq.heappush(candidate_station, (-fuel, next_destination))

        if candidate_station:
            s_fuel, _ = heapq.heappop(candidate_station)
            current_fuel -= s_fuel
            count += 1
        else:
            return -1

    return count


print(g_func(fuel_station, final_destination, current_fuel))
