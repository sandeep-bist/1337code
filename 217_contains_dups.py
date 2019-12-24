from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in
    the array, and it should return false if every element is distinct.
    """
    return len(nums) != len(set(nums))


arr = [1, 2, 3, 1]
print(contains_duplicate(arr))  # True

arr2 = [1, 2, 3]
print(contains_duplicate(arr2))  # False
