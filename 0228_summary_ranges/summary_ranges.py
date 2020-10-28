from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    i = 0
    while i < len(nums):
        tmp = nums[i]
        while (i + 1 < len(nums)) and nums[i + 1] - nums[i] == 1:
            i += 1
        if nums[i] == tmp:
            res.append(str(nums[i]))
        else:
            res.append(f"{tmp}->{nums[i]}")
        i += 1
    return res
