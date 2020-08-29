from typing import List


def pancake_sort(A: List[int]) -> List[int]:
    """
    Time: O(n**2)
    Space: O(n)
    """
    res = []
    for x in range(len(A), 1, -1):
        i = A.index(x)
        res.extend([i + 1, x])
        A = A[:i:-1] + A[:i]
    return res
