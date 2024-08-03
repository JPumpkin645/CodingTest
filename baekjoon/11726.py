def dp(x: int, v_list: list):
    if x <= 1:
        return 1
    if x <= 2:
        return 2
    if v_list[x] == 0:
        v_list[x] = dp(x - 1, v_list) + dp(x - 2, v_list)
    return v_list[x]


n = int(input())
v_list = [0] * 1001

print(dp(n, v_list=v_list) % 10007)
