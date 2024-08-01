import sys


def is_vps(x: str) -> bool:
    stack = []
    for i in x:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


n = int(input())
for _ in range(n):
    print("YES" if is_vps(sys.stdin.readline().rstrip()) else "NO")
