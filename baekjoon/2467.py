import sys

input = sys.stdin.readline

n = int(input())
l_list = list(map(int, input().split()))

left = 0
right = n - 1
answer = [left, right]
min_value = abs(l_list[left] + l_list[right])

while left < right:
    value = l_list[left] + l_list[right]
    abs_value = abs(value)

    if min_value > abs_value:
        min_value = abs_value
        answer = [left, right]
        if min_value == 0:
            break

    if value < 0:
        left += 1
    else:
        right -= 1

print(l_list[answer[0]], l_list[answer[1]])
