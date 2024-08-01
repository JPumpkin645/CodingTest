import sys
from collections import defaultdict

n = int(input())
card_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))

card_dict = defaultdict(int)

for card in card_list:
    card_dict[card] += 1

result = [card_dict[num] if num in card_dict else 0 for num in check_list]

print(*result)
