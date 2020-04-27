from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    """
    Time: O(m * n)
    Space: O(1)
    """
    res = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] = int(matrix[r][c])
            if matrix[r][c] and r and c:
                matrix[r][c] = min(matrix[r - 1][c], matrix[r - 1]
                                   [c - 1], matrix[r][c - 1]) + 1
            res = max(res, matrix[r][c])
    return res ** 2
