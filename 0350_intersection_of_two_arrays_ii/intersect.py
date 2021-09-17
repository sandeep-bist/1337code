from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    count = Counter(nums1)
    res = []
    for num in nums2:
        if count[num] > 0:
            res.append(num)
            count[num] -= 1
    return res