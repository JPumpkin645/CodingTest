import sys


def command(x: str, stack: list):
    if x.startswith("1"):
        _, n = x.split(" ")
        stack.append(n)
    elif x == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x == "3":
        print(len(stack))
    elif x == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif x == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)


n = int(input())
stack = []
for _ in range(n):
    command(sys.stdin.readline().rstrip(), stack=stack)
