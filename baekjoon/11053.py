# 6
# 10 20 10 30 20 50
# => 4

# 6
# 2 3 4 1 5 7
# => 5

# 9
# 2 3 4 1 5 9 8 9 10
# => 7


import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
values = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            values[i] = max(values[i], values[j] + 1)

print(max(values))
