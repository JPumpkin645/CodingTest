n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
answer = 0
for i in range(1, n + 1):
    answer += p_list[i - 1] * (n + 1 - i)

print(answer)
