import sys

ca_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

input_string = sys.stdin.readline().rstrip()
for a in ca_list:
    input_string = input_string.replace(a, "*")

print(len(input_string))
