def orderly_queue(s: str, k: int) -> str:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    return "".join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))