from typing import List


def generate(numRows: int) -> List[List[int]]:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    if not numRows:
        return []
    elif numRows == 1:
        return [[1]]
    res = [[1]]
    for i in range(1, numRows):
        tmp = [1]
        for j in range(1, i):
            tmp.append(res[i - 1][j - 1] + res[i - 1][j])
        tmp.append(1)
        res.append(tmp)
    return res
