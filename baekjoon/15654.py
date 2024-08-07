import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [0] + sorted(list(map(int, input().rstrip().split())))

stack = [[]]

while stack:
    array = stack.pop()

    if len(array) == m:
        print(*array)
        continue

    for i in range(n, 0, -1):
        if num_list[i] not in array:
            stack.append(array + [num_list[i]])
