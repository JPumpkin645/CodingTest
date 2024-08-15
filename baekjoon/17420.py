import math
import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

gifticon = sorted([rest, plan] for rest, plan in zip(a, b))

current_max = gifticon[0][0]
previous_plan = gifticon[0][1]
count = 0

for i in range(n):
    rest_days, plan_days = gifticon[i]

    if previous_plan > rest_days:
        times = math.ceil((previous_plan - rest_days) / 30)
        count += times
        rest_days += 30 * times

    current_max = max(current_max, rest_days)

    if i + 1 < n and plan_days != gifticon[i + 1][1]:
        previous_plan = max(current_max, gifticon[i + 1][1])

print(count)
