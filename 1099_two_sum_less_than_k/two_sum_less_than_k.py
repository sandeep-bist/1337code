from typing import List


def twoSumLessThanK(A: List[int], K: int) -> int:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    res = -1
    A.sort()
    lo, hi = 0, len(A) -1
    while lo < hi:
        if (A[lo] + A[hi] < K):
            res = max(res, A[lo] + A[hi])
            lo += 1
        else:
            hi -= 1
    return res