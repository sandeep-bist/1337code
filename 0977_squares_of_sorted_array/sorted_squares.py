from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    i, j = 0, len(nums) - 1
    res = [0] * len(nums)
    for p in range(len(nums) - 1, -1, -1):
        if abs(nums[i]) < abs(nums[j]):
            res[p] = nums[j] * nums[j]
            j -= 1
        else:
            res[p] = nums[i] * nums[i]
            i += 1
    return res
            
            