n, k = map(int, input().split())

coin_list = [int(input()) for _ in range(n)]
count = 0

for i in coin_list[::-1]:
    coin = k // i
    count += coin
    k %= i

print(count)
