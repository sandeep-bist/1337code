from typing import List


def string_shift(s: str, shift: List[List[int]]) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    left_sh = 0
    for direction, amount in shift:
        if direction == 1:
            amount = -amount
        left_sh += amount
    left_sh %= len(s)  # it will change negative to positive
    s = s[left_sh:] + s[:left_sh]
    return s
