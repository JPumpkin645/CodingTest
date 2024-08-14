import math
import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sort the gifticon list by plan date first, then by the rest days.
gifticon = sorted([rest, plan] for rest, plan in zip(a, b))

current_max = gifticon[0][0]
previous_plan = gifticon[0][1]
count = 0

for i in range(n):
    rest_days, plan_days = gifticon[i]

    # If the current plan date is greater than the current rest days, calculate the required increments.
    if previous_plan > rest_days:
        times = math.ceil((previous_plan - rest_days) / 30)
        count += times
        rest_days += 30 * times

    # Update current_max to the maximum rest days encountered so far.
    current_max = max(current_max, rest_days)

    # Update previous_plan only when moving to a new plan date.
    if i + 1 < n and plan_days != gifticon[i + 1][1]:
        previous_plan = max(current_max, gifticon[i + 1][1])

print(count)
