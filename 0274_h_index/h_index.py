from typing import List


def h_index(citations: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    size = len(citations)
    bucket = [0] * (size + 1)
    for c in citations:
        if c >= size:
            bucket[size] += 1
        else:
            bucket[c] += 1
    i = size
    res = 0
    while i >= 0:
        res += bucket[i]
        if res >= i:
            return i
        i -= 1
    return 0
