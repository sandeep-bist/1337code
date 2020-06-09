from typing import Dict, List
from collections import deque, defaultdict
from bisect import bisect_left


def is_subsequence(s: str, t: str) -> bool:
    """
    Time: O(m + n)
    Space: O(m)
    """
    if not s:
        return True
    d = deque(s)
    for char in t:
        if d and char == d[0]:
            d.popleft()
    return not len(d)

# Alternate solution for stream of S


def is_subsequence_bs(s: str, t: str) -> bool:
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    d = create_pos_map(t)
    lower_bound = 0
    for char in s:
        if char not in d:
            return False
        index_list = d[char]
        index = bisect_left(index_list, lower_bound)
        if index == len(index_list):
            return False
        lower_bound = index_list[index] + 1
    return True


def create_pos_map(s: str) -> Dict[str, List[int]]:
    d = defaultdict(list)
    for i, e in enumerate(s):
        d[e].append(i)
    return d
