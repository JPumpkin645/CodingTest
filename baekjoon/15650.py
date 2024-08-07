import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numList = [i for i in range(0, n + 1)]

stack = [([], 1)]

while stack:
    result, start = stack.pop()

    if len(result) == m:
        print(*result)
        continue

    for i in range(n, start - 1, -1):
        if len(result) == 0 or i > result[-1]:
            new_result = result + [numList[i]]
            stack.append((new_result, i + 1))
