from typing import List


def validMountainArray(arr: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    i, j = 0, len(arr)
    if j < 3:
        return False
    while i + 1 < j and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == j - 1:
        return False
    while i + 1 < j and arr[i] > arr[i + 1]:
        i += 1
    return i == j - 1