from typing import List


def minPatches(nums: List[int], n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    missing = 1
    i = 0
    patches = []
    while missing <= n:
        if i < len(nums) and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            patches.append(missing)
            missing += missing
    return len(patches)