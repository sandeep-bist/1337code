from typing import List


def shortest_distance(words: List[str], word1: str, word2: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    min_distance = len(words)
    i1 = i2 = -1
    for i, word in enumerate(words):
        if word == word1:
            i1 = i
        elif word == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            min_distance = min(min_distance, abs(i1 - i2))
    return min_distance
