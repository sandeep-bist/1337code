def is_palindrome(x: int) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    s = str(x)
    return s == s[::-1]
