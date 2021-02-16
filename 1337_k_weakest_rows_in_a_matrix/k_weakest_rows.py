from bisect import insort
from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    """
    Time: O(log(n) * m)
    Space: O(n * m)
    """
    res = []
    for index, row in enumerate(mat):
        ones = count_ones(row)
        insort(res, (ones, index))
    return [x[1] for x in res][:k]
    

def count_ones(arr: List[int]) -> int:
    i, j = 0, len(arr)
    while i < j:
        mid = (i + j) // 2
        if arr[mid] == 1:
            i = mid + 1
        else:
            j = mid
    return i
                