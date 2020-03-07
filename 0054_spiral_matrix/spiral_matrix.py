from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    res = []
    if not len(matrix):
        return res
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while True:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        if left > right or top > bottom:
            break
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if left > right or top > bottom:
            break
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        if left > right or top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        if left > right or top > bottom:
            break
    return res
