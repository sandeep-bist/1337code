def longest_palindrome(s: str) -> str:
    """
    Time: O(n**3)
    Space: O(n**3)
    """
    res = ""
    for i in range(len(s)):
        res = max(expand(s, i, i), expand(s, i, i + 1), res, key=len)
    return res


def expand(s: str, l: int, r: int) -> str:
    while 0 <= l and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]
