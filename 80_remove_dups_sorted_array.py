from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place such that
    duplicates appeared at most twice and return the new length.
    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.
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


arr = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(arr))  # 5
print(arr)  # [1,1,2,2,3]
