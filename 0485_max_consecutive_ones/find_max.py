from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = curr = 0
    for num in nums:
        if num == 1:
            curr += 1
            res = max(res, curr)
        else:
            curr = 0
    return res
            