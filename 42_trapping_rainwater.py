from typing import List


def trap(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the
    width of each bar is 1, compute how much water it is able to trap after
    raining.
    """
    l = 0
    r = len(height) - 1
    l_max = r_max = res = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] > l_max:
                l_max = height[l]
            else:
                res += l_max - height[l]
            l += 1
        else:
            if height[r] > r_max:
                r_max = height[r]
            else:
                res += r_max - height[r]
            r -= 1
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
"""
       |
   |   || |
_|_||_||||||
"""
print(trap(arr))  # 6
