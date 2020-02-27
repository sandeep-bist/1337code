from collections import deque
from typing import List


def bag_of_tokens_score(tokens: List[int], points: int):
    """
    You have an initial power P, an initial score of 0 points, and a bag of
    tokens.
    Each token can be used at most once, has a value token[i], and has
    potentially two ways to use it.
    If we have at least token[i] power, we may play the token face up, losing
    token[i] power, and gaining 1 point.
    If we have at least 1 point, we may play the token face down, gaining
    token[i] power, and losing 1 point.
    Return the largest number of points we can have after playing any number
    of tokens.
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


print(bag_of_tokens_score([100], 50))  # 0
print(bag_of_tokens_score([100, 200], 150))  # 1
print(bag_of_tokens_score([100, 200, 300, 400], 200))  # 2
