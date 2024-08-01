import sys

n, m = map(int, input().split())
not_seen_list = set(sys.stdin.readline().rstrip() for _ in range(n))
not_heard_list = set(sys.stdin.readline().rstrip() for _ in range(m))
not_seen_heard_list = not_seen_list.intersection(not_heard_list)

print(len(not_seen_heard_list))
print(*sorted(not_seen_heard_list), sep="\n")
