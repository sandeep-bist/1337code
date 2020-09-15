def length_of_last_word(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res, i = 0, len(s) - 1
    while i >= 0:
        if s[i] != ' ':
            res += 1
        elif res > 0:
            return res
        i -= 1
    return res
