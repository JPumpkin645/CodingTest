import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]

    if n >= 1:
        dp[0][1] = stickers[0][0]
        dp[1][1] = stickers[1][0]
    if n >= 2:
        dp[0][2] = stickers[1][0] + stickers[0][1]
        dp[1][2] = stickers[0][0] + stickers[1][1]
    if n >= 3:
        for i in range(3, n + 1):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i - 1]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i - 1]

    print(max(dp[1][n], dp[0][n]))
