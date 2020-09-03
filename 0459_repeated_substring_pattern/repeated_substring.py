def repeated_substring_pattern(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    size = len(s)
    dp = [0] * size
    for i in range(1, size):
        j = dp[i - 1]
        while j > 0 and s[i] != s[j]:
            j = dp[j - 1]
        if s[i] == s[j]:
            j += 1
        dp[i] = j
    last = dp[size - 1]
    return last != 0 and size % (size - last) == 0


def repeated_substring_pattern_alternate(s: str) -> bool:
    """
    Time: O(n**2)
    Space: O(n)
    """
    double = s * 2
    return s in double[1:-1]
