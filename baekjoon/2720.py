# 25/10/5/1
# greedy

total_input = int(input())

for _ in range(total_input):
    total_money = int(input())
    coin_list = [25, 10, 5, 1]
    answer_list = []
    for i in coin_list:
        answer_list.append(total_money // i)
        total_money %= i
    print(*answer_list)
