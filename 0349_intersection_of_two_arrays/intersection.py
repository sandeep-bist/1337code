from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    return set(nums1) & set(nums2)
