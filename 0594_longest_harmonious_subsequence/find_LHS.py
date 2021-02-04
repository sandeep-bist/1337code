from collections import defaultdict
from typing import List


def findLHS(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    hm = defaultdict(int)
    res = 0
    for n in nums:
        hm[n] += 1
        if n + 1 in hm:
            res = max(res, hm.get(n) + hm.get(n + 1))
        if n - 1 in hm:
            res = max(res, hm.get(n) + hm.get(n - 1))
    return res