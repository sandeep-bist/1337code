def buddyStrings(A: str, B: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    if len(A) != len(B):
        return False
    if A == B:
        return len(set(A)) < len(A)
    diff = [(a, b) for a, b in zip(A, B) if a != b]
    return len(diff) == 2 and diff[0] == diff[1][::-1]
