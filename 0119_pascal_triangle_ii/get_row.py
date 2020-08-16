from typing import List


def get_row(row_index: int) -> List[int]:
    """
    Time: O(n**2)
    Space: O(n)
    """
    res = [1]
    for i in range(1, row_index + 1):
        for j in range(len(res) - 1, 0, -1):
            res[j] = res[j - 1] + res[j]
        res.append(1)
    return res
