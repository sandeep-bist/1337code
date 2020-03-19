from bisect import bisect_left
from collections import defaultdict
from typing import Dict, List


def num_matching_subseq(S: str, words: List[str]) -> int:
    """
    Time: O(m + n * log(m))
    Space: O(n)
    """
    m = defaultdict(list)
    for i, ch in enumerate(S):
        m[ch].append(i)
    return sum(is_valid_str(m, w) for w in words)


def is_valid_str(m: Dict[str, List[int]], word: str) -> bool:
    i = -1
    for c in word:
        if c not in m:
            return False
        indexes = m[c]
        j = bisect_left(indexes, i)
        if j == len(indexes):
            return False
        else:
            i = indexes[j] + 1
    return True
