def valid(board: list, col: int, row: int, num: int):
    if num in board[row]:
        return False

    for i in range(9):
        if num == board[i][col]:
            return False

    row, col = 3 * (row // 3), 3 * (col // 3)
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == num:
                return False

    return True


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def s_func(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if valid(board, col, row, num):
            board[row][col] = num

            if s_func(board):
                return True

            board[row][col] = 0

    return False


board = [list(map(int, list(input()))) for _ in range(9)]

if s_func(board):
    for i in range(9):
        print(*board[i], sep="")
