from typing import List


def rob_again(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))


def rob(nums: List[int]) -> int:
    prev = curr = 0
    for i in nums:
        temp = max(i + prev, curr)
        prev = curr
        curr = temp
    return curr
