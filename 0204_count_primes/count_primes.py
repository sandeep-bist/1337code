def count_primes(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if n < 2:
        return 0
    s = [1] * n
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            for j in range(i * i, n, i):
                s[j] = 0
    return sum(s)
