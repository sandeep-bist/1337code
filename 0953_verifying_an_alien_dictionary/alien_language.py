from typing import List


def is_alien_sorted(words: List[str], order: str) -> bool:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    m = {c: i for i, c in enumerate(order)}
    for a, b in zip(words, words[1:]):
        # for cases such as ["apple", "app"]
        if a[:len(b)] == b and len(a) > len(b):
            return False
        for i, j in zip(a, b):
            if m[i] < m[j]:
                break
            if m[i] > m[j]:
                return False
    return True

