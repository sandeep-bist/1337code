def valid_palindrome(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            exclude_last = s[i: j]
            exclude_first = s[i + 1: j + 1]
            return is_palindrome(exclude_last) or is_palindrome(exclude_first)
        i += 1
        j -= 1
    return True


def is_palindrome(s: str):
    return s == s[::-1]
