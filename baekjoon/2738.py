import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
a = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    a.append(line)
b = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    b.append(line)

for i in range(n):
    buffur = ""
    for j in range(m):
        buffur += str(a[i][j] + b[i][j]) + " "
    print(buffur[:-1])
