def is_prime_number(x: int) -> bool:
    root_x = int(x**0.5)
    if x == 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, root_x + 1):
        if x % i == 0:
            return False
    return True


m = int(input())
n = int(input())

prime_number_list = []
for i in range(m, n + 1):
    if is_prime_number(i):
        prime_number_list.append(i)
if len(prime_number_list) == 0:
    print(-1)
else:
    print(sum(prime_number_list))
    print(prime_number_list[0])
