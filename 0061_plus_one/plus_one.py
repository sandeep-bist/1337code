from collections import deque
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    carry = 1
    for i in reversed(range(len(digits))):
        carry, digits[i] = divmod(digits[i]+carry, 10)
    if carry > 0:
        return [carry] + digits
    else:
        return digits


def plus_one_comp(digits: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    i = int("".join(str(x) for x in digits)) + 1
    return ([x for x in str(i)])
