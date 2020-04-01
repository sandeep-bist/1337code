from collections import Counter
from typing import List


def single_number(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    c = Counter(x for x in nums)
    for k, v in c.items():
        if v == 1:
            return k


def single_number_bitwise(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    once = twice = 0
    for i in nums:
        once = (i ^ once) & ~twice
        twice = (i ^ twice) & ~once
    return once
