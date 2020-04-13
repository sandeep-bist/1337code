from typing import List


def find_max_length(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    indexes = {0: -1}
    res = tmp = 0
    for i, e in enumerate(nums):
        tmp += 1 if e else -1
        res = max(res, i - indexes.setdefault(tmp, i))
    return res
