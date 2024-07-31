import sys

n = int(sys.stdin.readline().rstrip())
index_list = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    index_list[num] += 1

for i in range(10001):
    for _ in range(index_list[i]):
        if index_list[i] != 0:
            print(i)
