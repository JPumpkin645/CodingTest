import sys

word = sys.stdin.readline().rstrip()

part_list = set()

for i in range(1, len(word) + 1):
    for j in range(len(word) + 1 - i):
        part_list.add(word[j : j + i])

print(len(part_list))
