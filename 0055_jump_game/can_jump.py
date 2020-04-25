from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    m = 0
    for i, e in enumerate(nums):
        if i > m:
            return False
        m = max(m, i + e)
    return True
