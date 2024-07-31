import sys

n = int(input())
index_list = [[] for _ in range(51)]
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    index_list[len(word)].append(word)

for i in range(51):
    word_list = index_list[i]
    if len(word_list) != 0:
        word_list = list(set(word_list))
        word_list.sort()
        for j in word_list:
            print(j)
