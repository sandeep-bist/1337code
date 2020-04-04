from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Time: O(n)
    Space: O(1)
    """
    i = 0
    for j in range(len(nums)):
        if nums[j]:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0


def move_zeroes_alt(nums: List[int]) -> None:
    nums[:] = [i for i in nums if i != 0] + (nums.count(0) * [0])
