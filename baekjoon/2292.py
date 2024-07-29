# 1-1
# 2-7 6*1+1
# 3-19 6*3+1
# 4-37 6*6+1
# 5-61 6*10+1
# i 3*(i)(i-1)+1

n = int(input())
count = 1
max_num = 1
while n > max_num:
    count += 1
    max_num = 3 * count * (count - 1) + 1
print(count)
