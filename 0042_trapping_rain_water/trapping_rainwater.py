from typing import List


def trap(height: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
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
