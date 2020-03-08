from typing import List


def min_domino_rotations(A: List[int], B: List[int]) -> int:
    """
    Time: O(m + n)
    Space: O(1)
    """
    def check(x):
        a = b = 0
        for i in range(len(A)):
            if A[i] != x and B[i] != x:
                return -1
            elif A[i] != x:
                a += 1
            elif B[i] != x:
                b += 1
        return min(a, b)
    ops = check(A[0])
    if ops != -1 or A[0] == B[0]:
        return ops
    return check(B[0])
