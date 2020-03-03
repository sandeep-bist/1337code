def longest_palindrome(s: str) -> str:
    """
    Given a string s, find the longest palindromic substring in s. You may
    assume that the maximum length of s is 1000.
    """
    res = ""
    for i in range(len(s)):
        res = max(expand(s, i, i), expand(s, i, i + 1), res, key=len)
    return res


def expand(s: str, l: int, r: int) -> str:
    """
    Expands a string and returns the longest palindrome it can grow into.
    """
    while 0 <= l and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


print(longest_palindrome("babad"))  # "aba"
print(longest_palindrome("cbbd"))  # "bb"
