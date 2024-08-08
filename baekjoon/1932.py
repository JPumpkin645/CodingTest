import sys

input = sys.stdin.readline

n = int(input())
t_list = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]

if n >= 1:
    dp[0][0] = t_list[0][0]
if n >= 2:
    dp[1][0] = t_list[0][0] + t_list[1][0]
    dp[1][1] = t_list[0][0] + t_list[1][1]

if n >= 3:
    for i in range(2, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + t_list[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + t_list[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + t_list[i][j]

print(max(dp[n - 1]))
