from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Given a matrix of m x n elements (m rows, n columns), return all elements
    of the matrix in spiral order.
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


arr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_order(arr1))  # [1,2,3,6,9,8,7,4,5]
arr2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(spiral_order(arr2))  # [1,2,3,4,8,12,11,10,9,5,6,7]
