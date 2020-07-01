def arrange_coins(n: int) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    i, j = 0, n
    while i <= j:
        mid = (i + j) // 2
        k = mid * (mid + 1) // 2
        if k == n:
            return mid
        if n < k:
            j = mid - 1
        else:
            i = mid + 1
    return j
