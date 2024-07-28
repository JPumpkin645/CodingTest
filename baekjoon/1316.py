import sys

num = int(sys.stdin.readline().rstrip())
answer = num
for _ in range(num):
    input_string = sys.stdin.readline().rstrip()
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            pass
        elif input_string[i] in input_string[i + 1 :]:
            answer -= 1
            break

print(answer)
