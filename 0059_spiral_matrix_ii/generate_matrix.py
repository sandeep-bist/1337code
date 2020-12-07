from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    """
    Time: O(n**2)
    Space: O(1)
    """
    m = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n * n):
        m[i][j] = k + 1
        if m[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return m   