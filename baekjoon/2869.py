a, b, v = map(int, input().split(" "))

count = 0
count += 1
v -= a

day = v // (a - b) if v % (a - b) == 0 else v // (a - b) + 1

count += day

print(count)
