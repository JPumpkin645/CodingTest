import sys

n = int(input())
p_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

result = []


def p_fuction(x: int, y: int, n: int):
    color = p_list[y][x]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != p_list[j][i]:
                p_fuction(x, y, n // 2)
                p_fuction(x + n // 2, y, n // 2)
                p_fuction(x, y + n // 2, n // 2)
                p_fuction(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


p_fuction(0, 0, n)
print(result.count(0))
print(result.count(1))
