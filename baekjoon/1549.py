x, y, w, s = map(int, input().split())
answer = 0

across = min(x, y)
straight = abs(x - y)

if w > s:
    if straight % 2 != 0:
        answer = (across + (straight // 2) * 2) * s + w
    else:
        answer = (across + (straight // 2) * 2) * s

elif s < 2 * w:
    answer = across * s + straight * w

else:
    answer = (x + y) * w


print(answer)
