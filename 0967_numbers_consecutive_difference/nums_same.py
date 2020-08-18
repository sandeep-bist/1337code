from typing import List


def nums_same_consec_diff(n: int, k: int) -> List[int]:
    """
    Time: O(n * 2**n)
    Space: O(2**n)
    """
    if n == 1:
        return [x for x in range(10)]
    res = []
    for i in range(1, 10):
        dfs(n - 1, i, k, res)
    return res


def dfs(n: int, num: int, k: int, res: List[int]):
    if not n:
        res.append(num)
        return
    tail = num % 10
    digits = set([tail + k, tail - k])
    for digit in digits:
        if 10 > digit >= 0:
            dfs(n - 1, num * 10 + digit, k, res)
