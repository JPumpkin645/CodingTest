import sys

input = sys.stdin.readline

s = list(input().rstrip())
stack = []
result = []
for i in s:
    if i.isalpha():
        result.append(i)
    elif i == "(":
        stack.append(i)
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            result.append(stack.pop())
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            result.append(stack.pop())
        stack.append(i)
    else:
        while stack and stack[-1] != "(":
            result.append(stack.pop())
        stack.pop()
    # print(stack)
    # print(result)

while stack:
    result.append(stack.pop())

print(*result, sep="")
