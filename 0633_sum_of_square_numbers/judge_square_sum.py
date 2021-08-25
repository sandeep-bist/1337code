def judge_square_sum(c: int) -> bool:
    """
    Time: O(log(n))
    Space: O(1)
    """
    if c < 0:
        return False
    start, end = 0, int(c**0.5)
    while start <= end:
        curr = start**2 + end**2
        if curr == c:
            return True
        if curr < c:
            start += 1
        else:
            end -= 1
    return False
        