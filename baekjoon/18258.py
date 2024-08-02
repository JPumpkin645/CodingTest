import sys
from collections import deque


def command(x: str, que: deque) -> None:
    if "push" in x:
        _, n = x.split()
        que.append(int(n))
    elif x.startswith("p"):
        print(que.popleft() if que else -1)
    elif x.startswith("s"):
        print(len(que))
    elif x.startswith("e"):
        print(0 if que else 1)
    elif x.startswith("f"):
        print(que[0] if que else -1)
    elif x.startswith("b"):
        print(que[-1] if que else -1)


n = int(input())
que = deque()
for _ in range(n):
    command(sys.stdin.readline().rstrip(), que=que)
