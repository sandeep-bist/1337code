from typing import List


def max_distance(arrays: List[List[int]]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = 0
    _min = arrays[0][0]
    _max = arrays[0][-1]
    for arr in arrays[1:]:
        res = max(res, _max - arr[0], arr[-1] - _min)
        _min = min(_min, arr[0])
        _max = max(_max, arr[-1])
    return res
