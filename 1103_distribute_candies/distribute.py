from typing import List


def distribute_candies(candies: int, num_people: int) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = [0] * num_people
    i = 0
    count = 1
    while candies > 0:
        res[i % num_people] += count if count < candies else candies
        candies -= count
        count += 1
        i += 1
    return res
