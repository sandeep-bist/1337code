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
    Time: O(n)
    Space: O(n)
    """
    n = len(row) // 2
    dsu = DSU(n)
    for i in range(n):
        x = row[2 * i] // 2
        y = row[2 * i + 1] // 2
        if x != y:
            dsu.union(x, y)
    return dsu.count
