from typing import List

# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation


class BinaryMatrix():
    def get(self, x: int, y: int) -> int:
        pass

    def dimensions(self) -> List[int]:
        pass


def leftmost_column_with_one(binaryMatrix: 'BinaryMatrix') -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    r, c = binaryMatrix.dimensions()
    row, col = 0, c - 1
    res = -1
    while col >= 0 and row < r:
        if binaryMatrix.get(row, col) == 1:
            res = col
            col -= 1
        else:
            row += 1
    return res
