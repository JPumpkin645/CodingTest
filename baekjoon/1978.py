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


n = int(input())

input_list = list(map(int, input().split(" ")))
count = sum(1 for i in input_list if is_prime_number(i))
print(count)
