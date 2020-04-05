from collections import Counter


def first_uniq_char(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    c = Counter(s)
    for i, e in enumerate(s):
        if c[e] == 1:
            return i
    return -1
