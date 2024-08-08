import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [0] + sorted(list(map(int, input().split())))
results = set()
stack = [([], [False] * (n + 1))]


while stack:
    result, visited = stack.pop()

    if (len(result)) == m:
        results.add(tuple(result))
        continue

    for i in range(n, 0, -1):
        new_visited = visited.copy()
        if not visited[i]:
            new_visited[i] = True
            stack.append((result + [num_list[i]], new_visited))

for result in sorted(results):
    print(*result)
