from typing import List


def sort_array_by_parity(A: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 1:
            while i < j and A[j] % 2 == 1:
                j -= 1
            A[i], A[j] = A[j], A[i]
        i += 1
    return A
