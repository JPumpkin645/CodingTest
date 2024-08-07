import sys

input = sys.stdin.readline


def b_func(n, m):
    stack = [[]]

    while stack:
        current: list = stack.pop()

        if len(current) == m:
            print(*current)
            continue

        for i in range(n, 0, -1):
            if i not in current:
                stack.append(current + [i])


n, m = map(int, input().split())
b_func(n, m)
