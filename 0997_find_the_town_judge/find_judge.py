from typing import List


def find_judge(N: int, trust: List[List[int]]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if not len(trust):
        return N
    potential = {}
    disqualified = set()
    for a, b in trust:
        if b not in potential:
            potential[b] = 1
        else:
            potential[b] += 1
        disqualified.add(a)
    for k, v in potential.items():
        if k not in disqualified and v == N - 1:
            return k
    return -1
