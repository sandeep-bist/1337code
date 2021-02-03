def hammingWeight(n: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    res = 0
    while n:
        if n & 1:
            res += 1
        n >>= 1
    return res