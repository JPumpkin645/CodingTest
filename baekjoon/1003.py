def p_function(x: int, p_list: list) -> list:
    if x == 0:
        return [1, 0]
    elif x == 1:
        return [0, 1]
    else:
        if p_list[x]:
            return p_list[x]
        p_list[x] = [
            p_function(x - 1, p_list)[0] + p_function(x - 2, p_list)[0],
            p_function(x - 1, p_list)[1] + p_function(x - 2, p_list)[1],
        ]
        return p_list[x]


n = int(input())
for _ in range(n):
    m = int(input())
    p_list = [[] for _ in range(m + 1)]
    print(*p_function(m, p_list))
