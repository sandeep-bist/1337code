from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    small = big = float("inf")
    for n in nums:
        if n <= small:
            small = n
        elif n <= big:
            big = n
        else:
            return True
    return False