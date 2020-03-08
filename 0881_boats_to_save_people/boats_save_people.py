from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    people.sort()
    i = count = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        count += 1
    return count
