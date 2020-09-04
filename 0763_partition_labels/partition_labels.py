from typing import List


def partition_labels(S: str) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    last = {c: i for i, c in enumerate(S)}
    res = []
    j = anchor = 0
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            res.append(i - anchor + 1)
            anchor = i + 1
    return res
