angle_list = []

for _ in range(3):
    angle = int(input())
    angle_list.append(angle)
if sum(angle_list) != 180:
    print("Error")
else:
    angle_set = set(angle_list)
    if len(angle_set) == 1:
        print("Equilateral")
    elif len(angle_set) == 2:
        print("Isosceles")
    else:
        print("Scalene")
