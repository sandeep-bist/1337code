from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Time: O(log(m * n))
    Space: O(1)
    """
    m = len(matrix)
    if not m:
        return False
    n = len(matrix[0])
    i, j = 0, m * n - 1
    while i <= j:
        mid = (i + j) // 2
        mid_val = matrix[mid // n][mid % n]
        if mid_val == target:
            return True
        if mid_val < target:
            i = mid + 1
        else:
            j = mid - 1
    return False
