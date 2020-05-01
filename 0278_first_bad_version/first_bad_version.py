# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def first_bad_version(n: int):
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start
