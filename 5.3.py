def solve_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
            if col-row+i >= 0 and board[i][col-row+i] == 1:
                return False
            if col+row-i < n and board[i][col+row-i] == 1:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack([r[:] for r in board], row+1)
                board[row][col] = 0
    result = []
    board = [[0]*n for _ in range(n)]
    backtrack(board, 0)
    return result

solutions = solve_queens(8)
print(len(solutions))
print(solutions[0])
