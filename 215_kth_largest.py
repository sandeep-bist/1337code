from random import randint
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted array. Note that it is the kth
     largest element in the sorted order, not the kth distinct element.
    """
    size = len(nums)
    return select(nums, 0, size - 1, size - k)


def select(nums: List[int], l: int, r: int, k: int) -> int:
    """
    Quick-select algorithm.
    """
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
    """
    Partitions an array with random pivot.
    """
    pivot = nums[p]
    nums[p], nums[r] = nums[r], nums[p]
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[r], nums[i] = nums[i], nums[r]
    return i


arr = [3, 2, 1, 5, 6, 4]
print(find_kth_largest(arr, 2))  # 5
