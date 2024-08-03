import sys

n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
sum_list = [0]
for i in array:
    sum_list.append(sum_list[-1] + i)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    print(sum_list[e] - sum_list[s - 1])
