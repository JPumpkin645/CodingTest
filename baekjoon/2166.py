n = int(input())

x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

area: float = 0
for i in range(n):
    x1, y1 = x_list[i], y_list[i]
    x2, y2 = x_list[(i + 1) % n], y_list[(i + 1) % n]
    area += x1 * y2 - x2 * y1

area = round(abs(area) / 2, 1)
print(area)
