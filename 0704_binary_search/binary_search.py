from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Time: O(log(n))
    Space: (1)
    """
    i, j = 0, len(nums)
    while i < j:
        mid = (i + j) // 2
        val = nums[mid]
        if val == target:
            return mid
        if target < val:
            j = mid
        else:
            i = mid + 1
    return -1
