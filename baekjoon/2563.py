import sys

white_paper = [[0 for _ in range(100)] for _ in range(100)]

num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    for i in range(x, min(x + 10, 100)):
        for j in range(y, min(y + 10, 100)):
            white_paper[i][j] = 1

answer = sum(sum(row) for row in white_paper)

print(answer)
