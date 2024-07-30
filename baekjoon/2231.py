n = int(input())
for i in range(1, n + 1):
    m = i
    additional_value = sum(map(int, str(m)))
    if n == m + additional_value:
        print(m)
        break
    if m == n:
        print(0)
