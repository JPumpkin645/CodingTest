n = int(input())
input_list = []
for _ in range(n):
    input_list.append(int(input()))

input_list.sort()
for i in range(n):
    print(input_list[i])
