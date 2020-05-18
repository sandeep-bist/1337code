from collections import Counter


def check_inclusion(self, s1: str, s2: str) -> bool:
    """
    Time: O(s1 + s2)
    Space: O(s1 + s2)
    """
    first_count = Counter(s1)
    sec_count = Counter()
    for i, c in enumerate(s2):
        if first_count == sec_count:
            return True
        sec_count[c] += 1
        if i >= len(s1):
            sec_count[s2[i - len(s1)]] -= 1
            if sec_count[s2[i - len(s1)]] == 0:
                del sec_count[s2[i - len(s1)]]
    return first_count == sec_count
