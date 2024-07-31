n = int(input())
count = 0
word_length = 2
while n != count:
    for i in range(10**word_length, 10 ** (word_length + 1)):
        if "666" in str(i):
            count += 1
            if n == count:
                print(i)
                break
    word_length += 1
