import sys

table = [sys.stdin.readline().rstrip() for _ in range(5)]

max_length = max(len(word) for word in table)

transformed_table = [line + "*" * (max_length - len(line)) for line in table]

new_word = ""
for i in range(max_length):
    for j in range(5):
        if transformed_table[j][i] != "*":
            new_word += transformed_table[j][i]

print(new_word)
