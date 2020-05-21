from typing import List


def count_squares(matrix: List[List[int]]) -> int:
    """
    Time: O(m * n)
    Space: O(1)
    """
    res = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r and c and matrix[r][c]:
                matrix[r][c] = min(matrix[r - 1][c], matrix[r]
                                   [c - 1], matrix[r - 1][c - 1]) + 1
            res += matrix[r][c]
    return res
