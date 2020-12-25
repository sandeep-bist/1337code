from collections import defaultdict
from typing import List


def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    """
    Time: O(n * m)
    Space: O(n * m)
    """
    d = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            d[i + j].append(matrix[i][j])
    res = []
    for index, arr in d.items():
        if index % 2 == 0:
            res.extend([x for x in arr[::-1]])
        else:
            res.extend([x for x in arr])
    return res