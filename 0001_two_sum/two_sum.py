from typing import List


def two_sum(nums: List[int], target: List[int]) -> list:
    """
    Time: O(n)
    Space: O(n)
    """
    map = {}
    for i, e in enumerate(nums):
        compliment = target - e
        if compliment in map:
            return [map[compliment], i]
        else:
            map[e] = i
    return []
