from collections import Counter
from typing import List


def find_anagrams(self, s: str, p: str) -> List[int]:
    """
    Time: O(s + p)
    Space: O(s + p)
    """
    s_size, p_size = len(s), len(p)
    if p_size > s_size:
        return []
    res = []
    s_counter = Counter()
    p_counter = Counter(p)
    for i in range(s_size):
        s_counter[s[i]] += 1
        if i >= p_size:
            if s_counter[s[i - p_size]] == 1:
                del s_counter[s[i - p_size]]
            else:
                s_counter[s[i - p_size]] -= 1
        if s_counter == p_counter:
            res.append(i - p_size + 1)
    return res
