from typing import List


def max_area(height: List[int]) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the
    two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
    together with x-axis forms a container, such that the container contains
    the most water.
    You may not slant the container and n is at least 2.
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


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
print(max_area(arr))
