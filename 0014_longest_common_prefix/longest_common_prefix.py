from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Time: O(m * n)
    Space: O(1)
    """
    if not len(strs):
        return ""
    for i, e in enumerate(strs[0]):
        # Vertical scanning.
        for s in strs[1:]:
            if i >= len(s) or s[i] != e:
                return strs[0][:i]
    return strs[0]


def longest_common_prefix_zip(strs: List[str]) -> str:
    """
    Time: O(n * m)
    Space: O(n * m)
    """
    res = []
    for x in zip(*strs):
        if len(set(x)) == 1:
            res.append(x[0])
        else:
            break
    return "".join(res)
