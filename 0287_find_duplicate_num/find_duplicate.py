from typing import List


def find_duplicate(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    h = t = nums[0]
    while True:
        t, h = nums[t], nums[nums[h]]
        if h == t:
            break
    h = nums[0]
    while h != t:
        t, h = nums[t], nums[h]
        if h == t:
            break
    return h
