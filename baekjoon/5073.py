input_on = True
while input_on:
    a, b, c = map(int, input().split(" "))
    if a == 0:
        input_on = False
        break
    side_list = sorted([a, b, c])
    if side_list[0] + side_list[1] <= side_list[2]:
        print("Invalid")
    else:
        side_set = set(side_list)
        if len(side_set) == 1:
            print("Equilateral")
        elif len(side_set) == 2:
            print("Isosceles")
        else:
            print("Scalene")
