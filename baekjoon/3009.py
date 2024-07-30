from collections import defaultdict

x_dict = defaultdict(int)
y_dict = defaultdict(int)

for _ in range(3):
    x, y = map(int, input().split(" "))
    x_dict[x] += 1
    y_dict[y] += 1

answer = []
for i, v in x_dict.items():
    if v == 1:
        answer.append(i)
for i, v in y_dict.items():
    if v == 1:
        answer.append(i)

print(*answer)
