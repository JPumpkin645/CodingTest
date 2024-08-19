import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0
acc = 0

INF = 987654321
min_length = INF

while end < n:
    acc += arr[end]
    end += 1

    while acc >= s:
        min_length = min(min_length, end - start)
        acc -= arr[start]
        start += 1

print(min_length if min_length != INF else 0)
