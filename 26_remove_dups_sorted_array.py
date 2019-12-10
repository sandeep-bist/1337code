from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.
    """
    # changes array in place
    nums[:] = sorted(set(nums))
    return len(nums)


arr = [1, 1, 2]
print(removeDuplicates(arr))  # 2
print(arr)  # [1, 2]
