import sys

input = sys.stdin.readline

n = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(n))
dp = [[0] * (n) for _ in range(n)]
INF = 987654321


for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = INF
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1])

print(dp[0][n - 1])
