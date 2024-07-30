a, b, c = map(int, input().split(" "))

side_list = sorted([a, b, c])
if side_list[-1] >= sum(side_list[:2]):
    side_list[-1] = sum(side_list[:2]) - 1

print(sum(side_list))
