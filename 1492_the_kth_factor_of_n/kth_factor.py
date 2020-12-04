def kthFactor(n: int, k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    arr = []
    j = 0
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
            j += 1
        if j == k:
            return arr[-1]
    return -1
            