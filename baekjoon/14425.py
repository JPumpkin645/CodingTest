import sys

n, m = map(int, input().split())

word_list = [sys.stdin.readline().rstrip() for _ in range(n)]
check_list = [sys.stdin.readline().rstrip() for _ in range(m)]

count = 0

for i in check_list:
    if i in word_list:
        count += 1
print(count)
