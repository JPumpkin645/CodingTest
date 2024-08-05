import sys

n = int(input())
timeline = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
timeline.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for new_start, new_end in timeline:
    if end <= new_start:
        count += 1
        end = new_end
print(count)
