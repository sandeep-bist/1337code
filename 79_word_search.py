from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True
    return False


def dfs(board: List[List[str]], i: int, j: int, count: int, word: str):
    """
    Depth-first search.
    """
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


matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
print(exist(matrix, "ABCCED"))  # True
print(exist(matrix, "ABCD"))  # False
