n = int(input())
m = {}
MOD = 1000000007


def f_func(x: int):
    if x == 0:
        return 0
    if x == 1:
        return 1

    if x in m:
        return m[x]

    if x % 2 == 0:
        m[x] = (2 * f_func((x - 2) // 2) + f_func(x // 2)) * f_func(x // 2) % MOD
    else:
        m[x] = (f_func((x + 1) // 2) ** 2 + f_func((x - 1) // 2) ** 2) % MOD
    return m[x]


print(f_func(n))
