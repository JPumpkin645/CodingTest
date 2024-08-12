import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

stack = []

for i in s:
    stack.append(i)
    if "".join(stack[-len(bomb) :]) == bomb:
        del stack[-len(bomb) :]

print("".join(stack) if stack else "FRULA")
