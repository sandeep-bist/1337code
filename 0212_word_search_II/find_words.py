from collections import defaultdict
from typing import List


class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word


def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
    """
    Time: O(m * 4 * 3**L - 1) where M is the number of cells in the board
    and L is the maximum length of words
    Space: O(n)
    """
    res = []
    r, c = len(board), len(board[0])
    t = Trie()
    for w in words:
        t.insert(w)
    root = t.root
    for i in range(r):
        for j in range(c):
            dfs(board, root, i, j, "", res)
    return res


def dfs(board, node, r, c, curr, res):
    if node.is_word:
        res.append(curr)
        node.is_word = False
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return
    tmp = board[r][c]
    node = node.children.get(tmp)
    if not node:
        return
    board[r][c] = "#"
    dfs(board, node, r + 1, c, curr + tmp, res)
    dfs(board, node, r, c + 1, curr + tmp, res)
    dfs(board, node, r - 1, c, curr + tmp, res)
    dfs(board, node, r, c - 1, curr + tmp, res)
    board[r][c] = tmp
