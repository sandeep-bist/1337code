def reverse_words(self, s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    return " ".join(word[::-1] for word in s.split(" "))
