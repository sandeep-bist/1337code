from typing import List


def sort_colors(nums: List[int]):
    """
    Given an array with n objects colored red, white or blue, sort them
    in-place so that objects of the same color are adjacent, with the
    colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red,
    white, and blue respectively.
    Do not return anything, modify nums in-place instead.
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


arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print(arr)
# [0, 0, 1, 1, 2, 2]
