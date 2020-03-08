from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    """
    Time: O(2 * n * log(n) + n)
    Space: O(1)
    """
    g.sort()
    s.sort()
    res = 0
    while len(s):
        if not g:
            break
        c = s.pop(0)
        if c >= g[0]:
            g.pop(0)
            res += 1
    return res
