def p_function(x: int, v_list: list):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    if v_list[x] == 0:
        v_list[x] = p_function(x - 1, v_list) + p_function(x - 2, v_list) + p_function(x - 3, v_list)
    return v_list[x]


n = int(input())
v_list = [0 for _ in range(12)]


for _ in range(n):
    print(p_function(int(input()), v_list))
