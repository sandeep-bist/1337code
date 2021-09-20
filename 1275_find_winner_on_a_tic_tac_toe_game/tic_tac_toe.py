from typing import List


def tic_tac_toe(moves: List[List[int]]) -> str:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    board = [[None] * 3 for _ in range(3)]
    turn = "A"
    for x, y in moves:
        board[x][y] = turn
        if is_victory(board):
            return turn
        turn = "B" if turn == "A" else "A"
    return "Draw" if len(moves) == 9 else "Pending"
    

def is_victory(board):
    if (((board[0][0] == board[0][1] == board[0][2]) and board[0][0]) or
        ((board[0][0] == board[1][1] == board[2][2]) and board[0][0]) or
        ((board[0][0] == board[1][0] == board[2][0]) and board[0][0]) or
        ((board[2][0] == board[2][1] == board[2][2]) and board[2][2]) or
        ((board[0][2] == board[1][2] == board[2][2]) and board[2][2]) or
        ((board[0][1] == board[1][1] == board[2][1]) and board[1][1]) or
        ((board[0][2] == board[1][1] == board[2][0]) and board[1][1]) or
        ((board[1][0] == board[1][1] == board[1][2]) and board[1][1])):
        return True
    return False