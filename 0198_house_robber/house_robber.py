from typing import List


def rob(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    prev = curr = 0
    for i in nums:
        temp = max(i + prev, curr)
        prev = curr
        curr = temp
    return curr
