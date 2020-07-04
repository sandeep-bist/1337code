def nth_ugly_number(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = [1]
    u2 = u3 = u5 = 0
    while n > 1:
        ugly = min(2 * res[u2], 3 * res[u3], 5 * res[u5])
        res.append(ugly)
        if ugly == 2 * res[u2]:
            u2 += 1
        if ugly == 3 * res[u3]:
            u3 += 1
        if ugly == 5 * res[u5]:
            u5 += 1
        n -= 1
    return res[-1]