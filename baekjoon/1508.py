import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
position = list(map(int, input().split()))


def available(position: list, m: int, k: int, x: int) -> bool:
    count = 1
    last_index = 0

    for i in range(1, k):
        if position[i] - position[last_index] >= x:
            count += 1
            last_index = i
            if count >= m:
                return True
    return False


left = 1
right = position[-1] - position[0]
dist = 0
while left <= right:
    mid = (left + right) // 2
    if available(position, m, k, mid):
        dist = mid
        left = mid + 1
    else:
        right = mid - 1


answer = [0] * k
last_position_index = 0
count = 1
answer[last_position_index] = 1

for i in range(1, k):
    if position[i] - position[last_position_index] >= dist:
        last_position_index = i
        answer[last_position_index] = 1
        count += 1
        if count == m:
            break
print(*answer, sep="")
