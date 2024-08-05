import sys

n, m = map(int, input().split())
t_list = list(map(int, sys.stdin.readline().rstrip().split()))
start = 0
end = max(t_list)

result = 0
while start <= end:
    total_t = 0
    mid = (start + end) // 2
    for x in t_list:
        if x > mid:
            total_t += x - mid

    if total_t < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
