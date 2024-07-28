import sys

answer = 0
position = [0, 0]
for i in range(9):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    temp_answer = max(line)
    if temp_answer >= answer:
        answer = temp_answer
        position = [i + 1, line.index(answer) + 1]

print(answer)
print(*position)
