n = int(input())
line = 1
while n > line:
    n -= line
    line += 1

answer = [n, line - n + 1] if line % 2 == 0 else [line - n + 1, n]

print(*answer, sep="/")
