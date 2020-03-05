from typing import List


def is_alien_sorted(words: List[str], order: str) -> bool:
    """
    In an alien language, surprisingly they also use english lowercase
    letters, but possibly in a different order. The order of the
    alphabet is some permutation of lowercase letters.
    Given a sequence of words written in the alien language, and the
    order of the alphabet, return true if and only if the given words
    are sorted lexicographicaly in this alien language.
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


arr0 = ["hello", "leetcode"]
str0 = "hlabcdefgijkmnopqrstuvwxyz"
print(is_alien_sorted(arr0, str0))  # True

arr1 = ["apple", "app"]
str1 = "abcdefghijklmnopqrstuvwxyz"
print(is_alien_sorted(arr1, str1))  # False

arr2 = ["word", "world", "row"]
str2 = "worldabcefghijkmnpqstuvxyz"
print(is_alien_sorted(arr2, str2))  # False
