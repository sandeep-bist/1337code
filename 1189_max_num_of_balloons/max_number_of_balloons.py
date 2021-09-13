from collections import Counter


def max_number_of_balloons(text: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    str_count = Counter(text)
    balloon_count = Counter('balloon')
    return min(str_count[c] // balloon_count[c] for c in balloon_count)
       