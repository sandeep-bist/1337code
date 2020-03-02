from typing import List


def min_domino_rotations(A: List[int], B: List[int]) -> int:
    """
    In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
    the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
    each half of the tile.)
    We may rotate the i-th domino, so that A[i] and B[i] swap values.
    Return the minimum number of rotations so that all the values in A are the
    same, or all the values in B are the same.
    If it cannot be done, return -1.
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


print(min_domino_rotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))  # 2
print(min_domino_rotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))  # -1
