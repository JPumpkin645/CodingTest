import sys
from collections import defaultdict

read = sys.stdin.readline().rstrip().upper()

dict: dict = defaultdict(int)

for item in read:
    dict[item] += 1

max_value = max(dict.values())
answer = [key for key, value in dict.items() if value == max_value]

if len(answer) > 1:
    print("?")
else:
    print(answer[0])
