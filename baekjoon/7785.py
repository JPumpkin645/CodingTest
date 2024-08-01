import sys


def modify_entrance_log(members: set, name: str, log: str):
    if log == "enter":
        members.add(name)
    elif log == "leave":
        members.discard(name)


n = int(input())
members = set()
for _ in range(n):
    name, log = sys.stdin.readline().rstrip().split(" ")
    modify_entrance_log(members=members, name=name, log=log)

sorted_members = sorted(list(members), reverse=True)

print(*sorted_members, sep="\n")
