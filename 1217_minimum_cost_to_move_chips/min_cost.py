from typing import List


def minCostToMoveChips(position: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    even = odd = 0
    for pos in position:
        if pos % 2 == 0:
            even +=1
        else:
            odd += 1
    return min(odd, even)