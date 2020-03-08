from collections import Counter
from typing import List


def largest_unique_number(arr: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return max([k for k, v in Counter(arr).items()
                if v == 1], default=-1)
