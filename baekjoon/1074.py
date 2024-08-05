n, r, c = map(int, input().split())


def get_z_value(n: int, r: int, c: int) -> int:
    if n == 0:
        return 0
    division = 4 ** (n - 1)
    unit = 2 ** (n - 1)
    if r < unit:
        if c < unit:
            return 0 + get_z_value(n - 1, r, c)
        else:
            return division + get_z_value(n - 1, r, c % unit)
    else:
        if c < unit:
            return division * 2 + get_z_value(n - 1, r % unit, c)
        else:
            return division * 3 + get_z_value(n - 1, r % unit, c % unit)


print(get_z_value(n, r, c))
