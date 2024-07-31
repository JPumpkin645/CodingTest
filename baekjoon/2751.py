import sys

n = int(sys.stdin.readline().rstrip())
input_list = []
for _ in range(n):
    input_list.append(int(sys.stdin.readline().rstrip()))

input_list.sort()
for i in range(n):
    print(input_list[i])
