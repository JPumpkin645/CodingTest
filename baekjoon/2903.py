# 0-2
# 1-3
# 2-5
# 3-9
# 4-17
# 5-33


def point_in_line(x: int):
    if x == 0:
        return 2
    return point_in_line(x - 1) * 2 - 1


n = int(input())

print(point_in_line(n) ** 2)
