import sys

n = int(input())

coordinate_list = list(map(int, sys.stdin.readline().rstrip().split()))

filtered_coordinate_list = sorted(set(coordinate_list))

rank_dict = {value: idx for idx, value in enumerate(filtered_coordinate_list)}

p_coordinate_list = [rank_dict[coordinate] for coordinate in coordinate_list]

print(*p_coordinate_list)
