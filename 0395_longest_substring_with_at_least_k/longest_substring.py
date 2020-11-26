def longestSubstring(s: str, k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if len(s) < k:
        return 0
    c = min(set(s), key=s.count)
    if s.count(c) >= k:
        return len(s)
    return max(longestSubstring(t, k) for t in s.split(c))