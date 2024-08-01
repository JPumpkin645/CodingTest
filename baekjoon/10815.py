import sys

n = int(input())
card_list = set(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(input())
check_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

result = []

for num in check_list:
    if num in card_list:
        result.append(1)
    else:
        result.append(0)

print(*result)
