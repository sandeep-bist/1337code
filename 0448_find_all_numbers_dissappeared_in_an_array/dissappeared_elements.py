from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    for i in nums:
        index = abs(i) - 1
        if nums[index] > 0:
            nums[index] *= - 1
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res


def find_disappeared_numbers_alt(self, nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    return set(range(1, len(nums) + 1)) - set(nums)
