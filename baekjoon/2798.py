n, m = map(int, input().split())
card_list = list(map(int, input().split(" ")))

max_value = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            value = card_list[i] + card_list[j] + card_list[k]
            if value > max_value and value <= m:
                max_value = value

print(max_value)
