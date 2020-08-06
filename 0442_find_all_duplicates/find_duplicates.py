from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    res = []
    for num in nums:
        i = abs(num)
        if nums[i - 1] < 0:
            res.append(i)
        nums[i - 1] *= -1
    return res
