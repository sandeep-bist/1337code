from itertools import permutations
from typing import List


def largest_time_from_digits(A: List[int]) -> str:
    """
    Time: O(1)
    Space: O(1)
    """
    for a, b, c, d in permutations(sorted(A, reverse=True)):
        if a * 10 + b < 24 and c < 6:
            return f"{a}{b}:{c}{d}"
    return ''
