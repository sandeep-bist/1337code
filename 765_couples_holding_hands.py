from typing import List


class DSU:
    def __init__(self, n: int):
        """
        Disjoint Set constructor.
        """
        self.parents = [i for i in range(n)]
        self.count = 0

    def find(self, x: int) -> int:
        """
        Finds parent of element with path compression functionality.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        """
        Combines parent of two elements if they do not match.
        """
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x != par_y:
            self.count += 1
            self.parents[par_x] = par_y


def min_swaps_couples(row: List[int]) -> int:
    """
    N couples sit in 2N seats arranged in a row and want to hold hands. We
    want to know the minimum number of swaps so that every couple is sitting
    side by side. A swap consists of choosing any two people, then they stand
    up and switch seats.
    The people and seats are represented by an integer from 0 to 2N-1, the
    couples are numbered in order, the first couple being (0, 1), the second
    couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
    The couples' initial seating is given by row[i] being the value of the
    person who is initially sitting in the i-th seat.
    """
    n = len(row) // 2
    dsu = DSU(n)
    for i in range(n):
        x = row[2 * i] // 2
        y = row[2 * i + 1] // 2
        if x != y:
            dsu.union(x, y)
    return dsu.count


arr = [0, 2, 1, 3]
print(min_swaps_couples(arr))  # 1

arr2 = [3, 2, 0, 1]
print(min_swaps_couples(arr2))  # 0
