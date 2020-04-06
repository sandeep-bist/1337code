from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Time: O(n * k * log(k))
    Space: O(n * k)
    """
    d = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in d:
            d[sorted_word] = [word]
        else:
            d[sorted_word].append(word)
    return d.values()


def group_anagrams_alt(strs: List[str]) -> List[List[str]]:
    """
    Time: O(n * k)
    Space: O(n * k)
    """
    primes = {'a': 2,
              'b': 3,
              'c': 5,
              'd': 7,
              'e': 11,
              'f': 13,
              'g': 17,
              'h': 19,
              'i': 23,
              'j': 29,
              'k': 31,
              'l': 37,
              'm': 41,
              'n': 43,
              'o': 47,
              'p': 53,
              'q': 59,
              'r': 61,
              's': 67,
              't': 71,
              'u': 73,
              'v': 79,
              'w': 83,
              'x': 89,
              'y': 97,
              'z': 101
              }
    d = {}
    for word in strs:
        p = 1
        for c in word:
            p *= primes.get(c)
        key = str(p)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    return d.values()
