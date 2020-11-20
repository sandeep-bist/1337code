from typing import List


def search(nums: List[int], target: int) -> bool:
    """
    Time: O(log(n))
    Space: O(1)
    """
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return True
        while l < mid and nums[l] == nums[mid]: # tricky part
            l += 1
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False