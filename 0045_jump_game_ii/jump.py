from typing import List


def jump(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    jumps = curr_farthest = curr_end = 0
    goal = len(nums) - 1
    for i in range(goal):
        curr_farthest = max(curr_farthest, nums[i] + i)
        if i == curr_end:
            jumps += 1
            curr_end = curr_farthest
            if curr_end >= goal:
                break
    return jumps