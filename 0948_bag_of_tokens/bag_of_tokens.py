from collections import deque
from typing import List


def bag_of_tokens_score(tokens: List[int], points: int):
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    res = cur = 0
    d = deque(sorted(tokens))
    while d and (d[0] <= points or cur):
        if d[0] <= points:
            points -= d.popleft()
            cur += 1
        else:
            points += d.pop()
            cur -= 1
        res = max(res, cur)
    return res
