from typing import List


def missing_number(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    missing = len(nums)
    for i, e in enumerate(nums):
        missing ^= i ^ e
    return missing


def missing_number_gauss(nums: List[int]) -> int:
    missing = len(nums) * (len(nums) + 1) // 2
    return missing - sum(nums)
