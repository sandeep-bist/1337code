def solve_sudoku(board):
    """
    Time: O(9**n) where n is the number of empty cells
    Space: O(m * n)
    """
    if not board or len(board) == 0:
        return
    solve(board)
        
def solve(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == '.':
                return try_nums(board, r, c)
    return True

def try_nums(board, r, c):
    nums = "123456789"
    for num in nums:
        if is_valid_pos(board, r, c, num):
            board[r][c] = num
            if solve(board): 
                return True
            board[r][c] = '.'
    return False
    
def is_valid_pos(board, r, c, num):
    def is_valid_col():
        for i in range(9):
            if board[i][c] == num: 
                return False
        return True
    def is_valid_row():  
        for i in range(9):
            if board[r][i] == num:
                return False
        return True
    def is_valid_square():
        for i in range(9):
            if board[(r // 3) * 3 + (i // 3)][(c // 3) * 3 + (i % 3)] == num:
                return False    
        return True
    return is_valid_col() and is_valid_row() and is_valid_square()