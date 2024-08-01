import sys


def is_match(x: str) -> bool:
    stack = []
    for i in x:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        if i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


is_on = True
while is_on:
    x = sys.stdin.readline().rstrip()
    if len(x) == 1:
        is_on = False
        break
    print("yes" if is_match(x) else "no")
