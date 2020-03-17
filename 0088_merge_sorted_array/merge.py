from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Time: O(n)
    Space: O(1)
    """
    i, j, end = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[end] = nums1[i]
            i -= 1
        else:
            nums1[end] = nums2[j]
            j -= 1
        end -= 1
    while j >= 0:
        nums1[end] = nums2[j]
        j -= 1
        end -= 1
