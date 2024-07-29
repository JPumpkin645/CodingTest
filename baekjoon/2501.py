n, k = map(int, input().split(" "))
number_list = []
for i in range(1, n + 1):
    if n % i == 0:
        number_list.append(i)
try:
    print(number_list[k - 1])
except Exception:
    print("0")
