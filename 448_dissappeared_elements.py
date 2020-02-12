from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
    elements appear twice and others appear once. Find all the elements of
    [1, n] inclusive that do not appear in this array.
    O(n) time complexity, O(1) space complexity.
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
    Alternate solution.
    O(n) time complexity, O(n) space complexity.
    """
    return set(range(1, len(nums) + 1)) - set(nums)


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_disappeared_numbers(arr))  # [5, 6]
