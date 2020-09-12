from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    """
    Time: O((9! * k)/9 - k)
    Space: O(k)
    """
    res = []
    backtrack(res, [], k, n, 1)
    return res


def backtrack(res: List[List[int]], curr: List[int], k: int, n: int, start: int):
    if len(curr) > k:
        return
    if len(curr) == k and n == 0:
        res.append(list(curr))
        return
    for i in range(start, 10):
        if n - i >= 0:
            backtrack(res, curr + [i], k, n - i, i + 1)
