import sys

n = int(input())

member_list = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split(" ")
    member_list.append((int(age), name, i))

member_list.sort(key=lambda x: (x[0], x[2]))

for member in member_list:
    print(*member[:2])
