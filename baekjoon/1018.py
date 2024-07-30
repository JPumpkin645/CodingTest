def count_repaints(board, x, y, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != pattern[i][j]:
                count += 1
    return count


n, m = map(int, input().split())
board = [input() for _ in range(n)]

black_pattern = ["WBWBWBWB", "BWBWBWBW"] * 4
white_pattern = ["BWBWBWBW", "WBWBWBWB"] * 4

min_repaints = 64

for i in range(n - 7):
    for j in range(m - 7):
        repaints_black = count_repaints(board, i, j, black_pattern)
        repaints_white = count_repaints(board, i, j, white_pattern)
        min_repaints = min(min_repaints, repaints_black, repaints_white)

print(min_repaints)
