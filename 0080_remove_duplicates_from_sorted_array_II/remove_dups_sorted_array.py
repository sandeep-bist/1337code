from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    count = {}
    i = 0
    while i < len(nums):
        curr = nums[i]
        if curr in count and count.get(curr) > 1:
            nums.remove(curr)
        else:
            # get zero or increment
            count[curr] = count.get(curr, 0) + 1
            i += 1
    return len(nums)
