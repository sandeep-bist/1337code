from functools import reduce
from typing import List


def single_mumber(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    return reduce(lambda x, y: x ^ y, nums, 0)
