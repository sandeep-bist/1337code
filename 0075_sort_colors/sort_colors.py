from typing import List


def sort_colors(nums: List[int]):
    """
    Time: O(n)
    Space: O(1)
    """
    c = p0 = 0
    p2 = len(nums) - 1
    while c <= p2:
        if nums[c] == 0:
            nums[c], nums[p0] = nums[p0], nums[c]
            p0 += 1
            c += 1
        elif nums[c] == 1:
            c += 1
        else:
            nums[c], nums[p2] = nums[p2], nums[c]
            p2 -= 1
