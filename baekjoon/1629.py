a, b, c = map(int, input().split())


def m_func(a, b, c) -> int:
    if b == 1:
        return a % c
    else:
        if b % 2 == 1:
            return (m_func(a, b // 2, c) ** 2) * a % c
        else:
            return (m_func(a, b // 2, c) ** 2) % c


print(m_func(a, b, c))
