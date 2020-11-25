def smallestRepunitDivByK(K: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    remainder = 0
    for res in range(1, K + 1):
        remainder = (remainder * 10 + 1) % K
        if remainder == 0:
            return res
    return -1