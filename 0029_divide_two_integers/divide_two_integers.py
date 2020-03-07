def divide(dividend: int, divisor: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    INT_MAX = (2**31) - 1
    INT_MIN = -(2**31)
    sign = (dividend > 0) is (divisor > 0)
    x, y = abs(dividend), abs(divisor)
    res = 0
    while x >= y:
        tmp, i = y, 1
        while x >= tmp:
            x -= tmp
            res += i
            i <<= 1
            tmp <<= 1
    res = res if sign else -res
    return max(min(INT_MAX, res), INT_MIN)
