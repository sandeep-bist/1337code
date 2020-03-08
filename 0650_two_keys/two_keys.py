def min_steps(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if n <= 1:
        return 0
    for i in range(2, n+1):
        if n % i == 0:
            return min_steps(int(n / i)) + i
