n = int(input())

n = 1000 - n

while n > 0:
    a = n // 500
    n %= 500
    b = n // 100
    n %= 100
    c = n // 50
    n %= 50
    d = n // 10
    n %= 10
    e = n // 5
    n %= 5
    f = n // 1
    n %= 1

print(a + b + c + d + e + f)
