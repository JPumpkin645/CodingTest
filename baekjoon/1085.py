x, y, w, h = map(int, input().split(" "))

distance_x = min(x, w - x)
distance_y = min(y, h - y)

print(min(distance_x, distance_y))
