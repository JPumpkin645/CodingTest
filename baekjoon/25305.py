n, k = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort(reverse=True)
print(input_list[k - 1])
