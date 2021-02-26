from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    _min, _max, start, end, n = float("inf"), float("-inf"), -1, -1, len(nums)
    for i in range(n):
        _min = min(_min, nums[n - 1 - i])
        _max = max(_max, nums[i])
        if _max > nums[i]:
            end = i
        if _min < nums[n - 1 - i]:
            start = n - 1 - i
    if start == -1:
        return 0
    return end - start + 1