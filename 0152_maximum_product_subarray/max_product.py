from typing import List


def max_product(self, nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    max_so_far = min_so_far = res = nums[0]
    for num in nums[1:]:
        tmp_max = max(num, num * max_so_far, num * min_so_far)
        min_so_far = min(num, num * max_so_far, num * min_so_far)
        max_so_far = tmp_max
        res = max(res, max_so_far)
    return res
