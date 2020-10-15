from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


def reverse(nums: List[int], i: int, j: int):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1
