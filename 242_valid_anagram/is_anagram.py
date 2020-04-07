from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    return Counter(s) == Counter(t)
