def reverse_words(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    return " ".join(s.split()[::-1])
