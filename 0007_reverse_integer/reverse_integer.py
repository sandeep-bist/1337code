def reverse(x: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    s = [1, -1][x < 0]
    res = s * int(str(abs(x))[::-1])
    return res if res.bit_length() < 32 else 0
