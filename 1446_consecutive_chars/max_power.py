def maxPower(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = count = 1
    for i, e in enumerate(s[:len(s) - 1]):
        if s[i + 1] == e:
            count += 1
            res = max(res, count)
        else:
            count = 1
    return res
            