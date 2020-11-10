from typing import List


def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    return [[1 ^ i for i in reversed(row)] for row in A]