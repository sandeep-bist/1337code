from typing import List


def smallestDivisor(nums: List[int], threshold: int) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    def under_threshold(divisor) -> bool:
        return sum((num + divisor - 1) // divisor for num in nums) <= threshold

    left, right = 1, nums[-1]
    while left < right:
        mid = left + (right - left) // 2
        if under_threshold(mid):
            right = mid
        else:
            left = mid + 1
    return left