import sys

index_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().rstrip().split(" "))
answer = ""
while n:
    char = index_list[n % b]
    answer = char + answer
    n //= b
print(answer)
