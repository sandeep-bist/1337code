from typing import List


def rob_again(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed. All houses at this
    place are arranged in a circle. That means the first house is the neighbor
    of the last one. Meanwhile, adjacent houses have security system connected
    and it will automatically contact the police if two adjacent houses were
    broken into on the same night.
    Given a list of non-negative integers representing the amount of money of
    each house, determine the maximum amount of money you can rob tonight
    without alerting the police.
    """
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))


def rob(nums: List[int]) -> int:
    """
    Helper.
    """
    prev = curr = 0
    for i in nums:
        temp = max(i + prev, curr)
        prev = curr
        curr = temp
    return curr
