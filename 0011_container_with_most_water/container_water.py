from typing import List


def max_area(height: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    maximum = float("-inf")
    l = 0
    r = len(height) - 1
    while l < r:
        minimum = min(height[l], height[r])
        maximum = max(maximum, (r - l) * minimum)
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return maximum
