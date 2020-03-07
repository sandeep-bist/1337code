from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    return len(nums) != len(set(nums))
