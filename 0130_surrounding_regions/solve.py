from itertools import product
from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    Time: O(n * m)
    Space: O(n * m)

    """
    if not board or not board[0]:
        return
    r, c = len(board), len(board[0])
    borders = list(product(range(r), [0, c-1])) + \
        list(product([0, r-1], range(c)))
    while borders:
        i, j = borders.pop()
        if 0 <= i < r and 0 <= j < c and board[i][j] == 'O':
            board[i][j] = 'S'
            borders += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
    board[:] = [['XO'[c == 'S'] for c in row] for row in board]
