import sys

input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))

u_dp = [1] * (n + 1)
d_dp = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            u_dp[i] = max(u_dp[i], u_dp[j] + 1)
        elif arr[j] > arr[i]:
            d_dp[i] = max(d_dp[i], d_dp[j] + 1, u_dp[j] + 1)

print(max(u_dp + d_dp))
