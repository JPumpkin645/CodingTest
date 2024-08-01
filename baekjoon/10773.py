import sys


def command(x: str, stack: list):
    if x == "0":
        stack.pop()
    else:
        stack.append(int(x))


n = int(input())
stack = []
for _ in range(n):
    command(sys.stdin.readline().rstrip(), stack=stack)

print(sum(stack))
