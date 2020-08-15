from typing import List


def find_permutation(s: str) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    res = [x for x in range(1, len(s) + 2)]
    i = 0
    while i < len(s):
        j = i + 1
        while j - 1 < len(s) and s[j - 1] == "D":
            j += 1
        if j - i > 1:
            swap(res, i, j - 1)
        i = j
    return res


def swap(arr: List[int], i: int, j: int):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
