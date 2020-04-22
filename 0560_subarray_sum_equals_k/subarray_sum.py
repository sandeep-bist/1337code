from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    count = total = 0
    cache = defaultdict(int)
    cache[0] = 1
    for num in nums:
        total += num
        count += cache[total - k]
        cache[total] += 1
    return count
