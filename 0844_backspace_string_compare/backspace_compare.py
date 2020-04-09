from functools import reduce
from typing import List


def backspace_compare(S: str, T: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    return backspace(list(S)) == backspace(list(T))


def backspace(arr: List[str]) -> List[str]:
    i = len(arr) - 1
    count = 0
    while i >= 0:
        if count and arr[i] != "#":
            arr.pop(i)
            i -= 1
            count -= 1
        elif arr[i] != "#":
            i -= 1
            continue
        while i >= 0 and arr[i] == "#":
            arr.pop(i)
            i -= 1
            count += 1
    return arr


def backspace_compare_reduce(S: str, T: str) -> bool:
    return reduce(build, S, []) == reduce(build, T, [])


def build(res: List[str], c: str) -> List[str]:
    if c != "#":
        res.append(c)
    elif res:
        res.pop()
    return res
