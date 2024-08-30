import sys

input = sys.stdin.readline

t = int(input())


def func(k_list):
    k = len(k_list)
    dp = [[0] * k for _ in range(k)]
    sum_arr = [0 for _ in range(k + 1)]
    INF = 987654321

    for i in range(k):
        sum_arr[i + 1] = sum_arr[i] + k_list[i]

    for length in range(2, k + 1):
        for i in range(k - (length - 1)):
            j = i + length - 1
            dp[i][j] = INF
            for mid in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + (sum_arr[j + 1] - sum_arr[i]))

    return dp[0][k - 1]


for _ in range(t):
    k = int(input())
    k_list = list(map(int, input().split()))
    answer = func(k_list)
    print(answer)
