from collections import defaultdict


def lengthOfLongestSubstringTwoDistinct(s: str):
    """
    Time: O(n)
    Space: O(1)
    """
    left = right = 0
    counts = defaultdict(int)
    while right < len(s):
        counts[s[right]] += 1
        right += 1
        if len(counts) > 2:
            counts[s[left]] -= 1
            if not counts[s[left]]:
                del counts[s[left]]
            left += 1
    return right - left