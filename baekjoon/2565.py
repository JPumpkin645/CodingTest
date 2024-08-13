import sys

input = sys.stdin.readline
n = int(input())
arr = [0]
v_dict = {}
for _ in range(n):
    start, end = map(int, input().split())
    arr.append(start)
    v_dict[start] = end

arr.sort()
u_dp = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if v_dict[arr[i]] > v_dict[arr[j]]:
            u_dp[i] = max(u_dp[i], u_dp[j] + 1)

print(n - max(u_dp))
