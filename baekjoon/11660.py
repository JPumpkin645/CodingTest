import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix_sum[i][j] = matrix_sum[i][j - 1] + matrix_sum[i - 1][j] - matrix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix_sum[x2][y2] - matrix_sum[x1 - 1][y2] - matrix_sum[x2][y1 - 1] + matrix_sum[x1 - 1][y1 - 1])
