from typing import List


def smallestRangeII(A: List[int], K: int) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    A.sort()
    MIN, MAX = A[0], A[-1]
    res = MAX - MIN
    for i in range(len(A) - 1):
        cur, nex = A[i], A[i + 1]
        res = min(res, (max(cur + K, MAX - K) - min(nex - K, MIN + K)))
    return res