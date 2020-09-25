from functools import cmp_to_key
from typing import List


def compare(a, b):
    x, y = a + b, b + a
    if x == y:
        return 0
    return 1 if x > y else -1


def largest_number(nums: List[int]) -> str:
    """
    Time: O(n(log n))
    Space: O(n)
    """
    strings = [str(x) for x in nums]
    strings.sort(key=cmp_to_key(compare), reverse=True)
    return str(int(''.join(strings)))
