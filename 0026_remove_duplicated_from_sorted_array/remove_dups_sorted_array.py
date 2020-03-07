from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Time: O(n log(n))
    Space: O(n)
    """
    # changes array in place
    nums[:] = sorted(set(nums))
    return len(nums)
