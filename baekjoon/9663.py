n = int(input())
# i번째 행에 몇 열에 퀸이 있는지 (인자: x값)
board = [-1] * n
columns = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)


def is_safe(column: int, row: int, columns: list, diag1: list, diag2: list):
    if columns[column]:
        return False
    if diag1[row - column]:
        return False
    if diag2[row + column]:
        return False
    return True


stack = [(0, board[:], columns[:], diag1[:], diag2[:])]
count = 0

while stack:
    row, c_board, c_columns, c_diag1, c_diag2 = stack.pop()

    if row == n:
        count += 1
        continue

    for column in range(n - 1, -1, -1):
        if is_safe(column, row, c_columns, c_diag1, c_diag2):
            c_columns[column] = True
            c_diag1[row - column] = True
            c_diag2[row + column] = True
            c_board[row] = column

            stack.append((row + 1, c_board[:], c_columns[:], c_diag1[:], c_diag2[:]))

            c_columns[column] = False
            c_diag1[row - column] = False
            c_diag2[row + column] = False


print(count)
