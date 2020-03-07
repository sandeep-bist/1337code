from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Time:    O(n * 4**L) where L is the length of the word
    Space:   O(L)
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True
    return False


def dfs(board: List[List[str]], i: int, j: int, count: int, word: str):
    if count == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or\
            board[i][j] != word[count]:
        return False
    tmp = board[i][j]
    board[i][j] = " "
    found = (dfs(board, i + 1, j, count + 1, word) or
             dfs(board, i, j + 1, count + 1, word) or
             dfs(board, i - 1, j, count + 1, word) or
             dfs(board, i, j - 1, count + 1, word))
    board[i][j] = tmp
    return found
