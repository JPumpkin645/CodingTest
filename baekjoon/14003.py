import sys

input = sys.stdin.readline


def binary_search(tails, target, high):
    low = 0
    while low != high:
        mid = (low + high) // 2
        if tails[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


n = int(input())
array = list(map(int, input().split()))

tails = [0] * n
size = 0

for x in array:
    if size == 0 or x > tails[size - 1]:
        tails[size] = x
        size += 1
    else:
        posision = binary_search(tails, x, size)
        tails[posision] = x

print(size)
