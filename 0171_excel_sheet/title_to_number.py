def title_to_number(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = 0
    for i, e in enumerate(s[::-1]):
        res += (ord(e) - 64) * 26**i
    return res
