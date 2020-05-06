from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    count = 0
    candidate = None
    for n in nums:
        if not count:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate
