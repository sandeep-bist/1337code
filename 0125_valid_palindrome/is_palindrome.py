def is_palindrome(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    s = [c for c in s.lower() if c.isalnum()]
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
