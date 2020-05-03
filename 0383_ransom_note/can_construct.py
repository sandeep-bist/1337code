from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    c = Counter(magazine)
    for s in ransomNote:
        if s not in c or not c[s]:
            return False
        c[s] -= 1
    return True
