def longest_palindrome(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = 0
    d = defaultdict(int)
    for char in s:
        d[char] += 1
        if d.get(char) == 2:
            res += 2
            d[char] = 0
    return res if res == len(s) else res + 1
