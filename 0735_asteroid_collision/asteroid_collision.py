from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    for a in asteroids:
        while len(res) and (a < 0 and res[-1] > 0):
            if -a == res[-1]:
                res.pop()
                break
            elif -a > res[-1]:
                res.pop()
                continue
            else:
                # breaking out of while-else does not result in else
                break
        else:
            res.append(a)
    return res
