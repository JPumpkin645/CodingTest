import sys

index_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = sys.stdin.readline().rstrip().split(" ")
b = int(b)

# answer = 0
# for i in range(len(n)):
#     answer += b ** (len(n) - 1 - i) * index_list.index(n[i])

answer = int(n, b)

print(answer)
