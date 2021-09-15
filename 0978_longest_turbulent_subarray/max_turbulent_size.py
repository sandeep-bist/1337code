from typing import List


def max_turbulence_size(arr: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = dec = inc = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            inc = dec + 1
            dec = 1
        elif arr[i] < arr[i - 1]:
            dec = inc + 1
            inc = 1
        else:
            dec = inc = 1
        res = max(res, max(dec, inc))
    return res