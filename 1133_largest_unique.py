from collections import Counter
from typing import List


def largest_unique_number(arr: List[int]) -> int:
    """
    Given an array of integers arr, return the largest integer that only
    occurs once.
    If no integer occurs once, return -1.
    """
    return max([k for k, v in Counter(arr).items() if v == 1], default=-1)


arr = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(largest_unique_number(arr))  # 8

arr2 = [9, 9, 8, 8]
print(largest_unique_number(arr2))  # -1
