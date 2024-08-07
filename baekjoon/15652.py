import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [i for i in range(n + 1)]

stack = [([], 1)]

while stack:
    current, index = stack.pop()

    if len(current) == m:
        print(*current)
        continue

    for i in range(n, index - 1, -1):
        if not current:
            stack.append((current + [num_list[i]], index))
        else:
            if current[-1] == num_list[i]:
                stack.append((current + [num_list[i]], index))
            elif current[-1] < num_list[i]:
                stack.append((current + [num_list[i]], index + 1))
