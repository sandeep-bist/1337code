def numberOfSteps(num: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    res = 0
    while num:
        if num & 1:
            num -= 1
        else:
            num //= 2
        res += 1
    return res
        