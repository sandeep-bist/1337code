from collections import Counter


def balance_string_split(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    splits = 0
    c = Counter()
    for i in s:
        c[i] += 1
        if c['R'] == c['L']:
            splits += 1
            c.clear()
    return splits
