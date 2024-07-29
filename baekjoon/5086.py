input_on = True
while input_on:
    a, b = map(int, input().split(" "))
    if a == 0 and b == 0:
        input_on = False
        break
    if b % a == 0:
        print("factor")
        pass
    elif a % b == 0:
        print("multiple")
        pass
    else:
        print("neither")
