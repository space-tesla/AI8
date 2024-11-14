# Q.2 Write a Python program to solve the N x N Queen problem.

def display_board(board):
    for row in board:
        print(" ".join(str(col) for col in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_queens(board, row):
    if row == len(board):
        display_board(board)
        return True
    res = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_queens(board, row + 1) or res
            board[row][col] = 0
    return res

N = int(input("Enter the size of the board (N): "))
board = [[0] * N for _ in range(N)]

if not solve_queens(board, 0):
    print("Solution does not exist.")
