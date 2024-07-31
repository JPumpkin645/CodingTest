n = str(input())
n_list = [int(i) for i in n]
n_list.sort(reverse=True)
print(*n_list, sep="")
