import sys

n = int(input())
score_list = [0] * 301
for i in range(1, n + 1):
    score_list[i] = int(sys.stdin.readline().rstrip())
ac_list = [0] * 301
ac_list[1] = score_list[1]
ac_list[2] = score_list[1] + score_list[2]
ac_list[3] = max(score_list[1] + score_list[3], score_list[2] + score_list[3])

for i in range(4, n + 1):
    ac_list[i] = max(ac_list[i - 3] + score_list[i - 1] + score_list[i], ac_list[i - 2] + score_list[i])

print(ac_list[n])
