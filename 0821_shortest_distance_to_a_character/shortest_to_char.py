from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    """
    Time: O(n)
    Spac: O(n)
    """
    prev = float('-inf')
    res = []
    for i, char in enumerate(s):
        if char == c:
            prev = i
        res.append(i - prev)
    prev = float('inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], prev - i)
    return res