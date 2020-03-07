from typing import List


class DSU:
    def __init__(self):
        """
        Disjoint Set constructor.
        """
        self.parents = {}
        self.count = 0

    def find(self, x: int) -> int:
        """
        Finds parent of element with path compression functionality.
        """
        if self.parents.get(x) != x:
            self.parents[x] = self.find(self.parents.get(x))
        return self.parents.get(x)

    def union(self, x: int, y: int):
        """
        Combines parent of two elements if they do not match.
        """
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x != par_y:
            self.count -= 1
            self.parents[par_x] = par_y

    def add(self, x: int):
        """
        Adds an element into DSU.
        """
        if x in self.parents:
            return
        self.parents[x] = x
        self.count += 1


def num_islands2(m: int, n: int, positions: List[List[int]]):
    """
    Time: O(m * n + L) where L is the number of operations
    Space: O(m * n)
    """
    surroundings = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dsu = DSU()
    res = []
    for pos in positions:
        # Creates a arbitrary key based on coordinates.
        key = pos[0] * n + pos[1]
        dsu.add(key)
        for s in surroundings:
            row, col = pos[0] + s[0], pos[1] + s[1]
            if 0 <= row < m and 0 <= col < n and row * n + col in dsu.parents:
                dsu.union(key, row * n + col)
        res.append(dsu.count)
    return res
