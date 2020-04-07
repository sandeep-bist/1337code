from typing import List


def count_elements(arr: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return sum(1 for x in arr if x + 1 in set(arr))
