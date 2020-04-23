def range_bitwise_and(m: int, n: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    shifts = 0   
    # find the common prefix
    while m < n:
        m = m >> 1
        n = n >> 1
        shifts += 1
    return m << shifts