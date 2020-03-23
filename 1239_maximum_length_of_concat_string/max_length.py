from typing import List


def max_length(arr: List[str]) -> int:
    """
    Time: O(2**n)
    Space: O(n)
    """
    res = [0]
    dfs(arr, 0, "", res)
    return res[0]


def dfs(arr: List[str], index: int, tmp: str, res: List[int]):
    if index == len(arr):
        if unique_chars(tmp) > res[0]:
            res[0] = len(tmp)
        return
    # Simulate adding current string and not
    dfs(arr, index + 1, tmp, res)
    dfs(arr, index + 1, tmp + arr[index], res)


def unique_chars(s):
    size = len(s)
    if size > len(set(s)):
        return -1
    return size

# WAYYY FASTER


def max_length_again(arr: List[str]) -> int:
    res = [set()]
    for a in arr:
        if len(a) > len(set(a)):
            continue
        a = set(a)
        for r in res[:]:
            if a & r:
                continue
            res.append(a | r)
    return max(len(s) for s in res)
