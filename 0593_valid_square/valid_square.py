from itertools import combinations
from typing import List

def validSquare(p1: List[int],
                p2: List[int],
                p3: List[int],
                p4: List[int]) -> bool:
    """
    Time: O(1)
    Spac: O(1)
    """
    hs = set(map(get_dist, combinations((p1, p2, p3, p4), 2)))
    return len(hs) == 2 and 0 not in hs 

def get_dist(pt: List[int]) -> int:
    a, b = pt
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2