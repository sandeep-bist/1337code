from collections import Counter
from typing import List


def total_fruit(tree: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = i = 0
    count = Counter()
    for j, e in enumerate(tree):
        count[e] += 1
        while len(count) > 2:
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1
        res = max(res, j - i + 1)
    return res
