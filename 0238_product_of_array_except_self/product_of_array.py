from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    size = len(nums)
    res = [1] * size
    pi = pj = 1
    for i in range(size):
        j = -1 - i
        res[i] *= pi
        res[j] *= pj
        pi *= nums[i]
        pj *= nums[j]
    return res
