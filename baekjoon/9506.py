input_on = True


def get_num_list(n: int) -> list:
    num_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            num_list.append(i)
    return num_list


while input_on:
    n = int(input())
    if n == -1:
        input_on = False
        break
    num_list = get_num_list(n)[:-1]
    summation = sum(num_list)
    if n == summation:
        print(n, "=", end=" ")
        print(*num_list, sep=" + ")
    else:
        print(n, "is NOT perfect.")
