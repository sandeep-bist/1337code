from random import randint
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    size = len(nums)
    return select(nums, 0, size - 1, size - k)


def select(nums: List[int], l: int, r: int, k: int) -> int:
    if l == r:
        return nums[l]
    random = randint(l, r)
    p = partition(nums, l, r, random)
    if k == p:
        return nums[k]
    elif k < p:
        return select(nums, l, p - 1, k)
    else:
        return select(nums, p + 1, r, k)


def partition(nums: List[int], l: int, r: int, p: int) -> int:
    pivot = nums[p]
    nums[p], nums[r] = nums[r], nums[p]
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[r], nums[i] = nums[i], nums[r]
    return i
