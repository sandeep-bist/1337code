from typing import List


def numberOfArithmeticSlices(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = curr = 0
    for i in range(2, len(A)):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            curr += 1
            res += curr
        else:
            curr = 0
    return res