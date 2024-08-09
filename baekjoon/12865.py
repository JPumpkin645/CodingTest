import sys

input = sys.stdin.readline

n, k = map(int, input().split())

packages = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if packages[i][0] <= j:
            dp[j][i] = max(dp[j][i - 1], dp[j - packages[i][0]][i - 1] + packages[i][1])
        else:
            dp[j][i] = dp[j][i - 1]

print(dp[k][n])
