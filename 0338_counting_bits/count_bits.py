from typing import List


def count_bits(self, num: int) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = [0]
    offset = 1
    for i in range(1, num + 1):
        if offset * 2 == i:
            offset *= 2
        res.append(res[i - offset] + 1)
    return res
