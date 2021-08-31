from math import prod
from typing import List


def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return prod([min(z) for z in zip(*ops)]) if ops else m * n