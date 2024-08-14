import sys

input = sys.stdin.readline

n = int(input())
ramen = list(map(int, input().split())) + [0, 0]
count = 0
for i in range(n):
    if ramen[i + 1] > ramen[i + 2]:
        case_2 = min(ramen[i], ramen[i + 1] - ramen[i + 2])
        ramen[i] -= case_2
        ramen[i + 1] -= case_2
        count += case_2 * 5

        case_3 = min(ramen[i], min(ramen[i + 1], ramen[i + 2]))
        ramen[i] -= case_3
        ramen[i + 1] -= case_3
        ramen[i + 2] -= case_3
        count += case_3 * 7
    else:
        case_3 = min(ramen[i], min(ramen[i + 1], ramen[i + 2]))
        ramen[i] -= case_3
        ramen[i + 1] -= case_3
        ramen[i + 2] -= case_3
        count += case_3 * 7

        case_2 = min(ramen[i], ramen[i + 1])
        ramen[i] -= case_2
        ramen[i + 1] -= case_2
        count += case_2 * 5

    case_1 = ramen[i]
    ramen[i] -= case_1
    count += case_1 * 3

print(count)
