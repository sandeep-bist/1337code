from typing import List


def longestMountain(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    N = len(A)
    res = base = 0
    while base < N:
        end = base
        if end + 1 < N and A[end] < A[end + 1]:
            while end+1 < N and A[end] < A[end+1]:
                end += 1
            if end + 1 < N and A[end] > A[end + 1]:
                while end+1 < N and A[end] > A[end+1]:
                    end += 1
                res = max(res, end - base + 1)
        base = max(end, base + 1)
    return res