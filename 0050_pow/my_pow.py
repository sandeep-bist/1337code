def my_pow(x: float, n: int) -> float:
    """
    Time: O(log(n))
    Space: O(1)
    """
    res, tmp = 1, abs(n)
    while tmp:
        if tmp & 1:
            res *= x
        x *= x
        tmp >>= 1
    return res if n > 0 else 1 / res
