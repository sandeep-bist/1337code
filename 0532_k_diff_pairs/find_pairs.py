from collections import Counter
from typing import List


def find_pairs(nums: List[int], k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    c = Counter(nums)
    res = 0
    for key in c.keys():
        if (k > 0 and key + k in c) or (k == 0 and c.get(key) > 1):
            res += 1
    return res
