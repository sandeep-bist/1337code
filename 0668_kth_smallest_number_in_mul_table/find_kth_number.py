def findKthNumber(m: int, n: int, k: int):
    """
    Time: O(m*log(m*n))
    Space: O(1)
    """
    def get_count(x):
        count = 0
        for i in range(1, m + 1):
            count += min(x // i, n)
        return count

    lo, hi = 1, m * n
    while lo < hi:
        mid = (lo + hi) // 2
        if get_count(mid) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo  
