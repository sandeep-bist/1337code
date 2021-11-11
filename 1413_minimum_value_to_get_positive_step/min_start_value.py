from typing import List


def minStartValue(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = curr = 0
    for num in nums:
        curr += num
        res = min(res, curr)
    return -res + 1