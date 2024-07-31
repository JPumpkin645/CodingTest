n = int(input())
currency_list = [3, 5]
large_num = 5001
d = [large_num] * (n + 1)

d[0] = 0

for i in range(len(currency_list)):
    for j in range(currency_list[i], n + 1):
        if d[j - currency_list[i]] != large_num:
            d[j] = min(d[j], d[j - currency_list[i]] + 1)

if d[n] == large_num:
    print(-1)
else:
    print(d[n])
