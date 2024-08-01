import sys

n, m = map(int, input().split(" "))

p_dict = {}

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    p_dict[str(i)] = name
    p_dict[name] = str(i)

for _ in range(m):
    key = sys.stdin.readline().rstrip()
    print(p_dict[key])
