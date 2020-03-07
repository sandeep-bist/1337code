from collections import Counter


def frequency_sort(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    return ("".join(char * times for char, times in Counter(s).most_common()))
    