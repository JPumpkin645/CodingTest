import sys


def command(s: str, x: set):
    if s.startswith("add"):
        _, new = s.split()
        x.update(set([int(new)]))
    elif s.startswith("remove"):
        _, new = s.split()
        x.difference_update(set([int(new)]))
    elif s.startswith("check"):
        _, new = s.split()
        if int(new) in x:
            print(1)
        else:
            print(0)
    elif s.startswith("toggle"):
        _, new = s.split()
        if int(new) in x:
            x.remove(int(new))
        else:
            x.add(int(new))
    elif s.startswith("all"):
        x.update(set(range(1, 21)))
    elif s.startswith("empty"):
        x.clear()


n = int(input())
result = set()
for _ in range(n):
    command(sys.stdin.readline().rstrip(), result)
