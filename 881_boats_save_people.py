from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    """
    The i-th person has weight people[i], and each boat can carry a maximum
    weight of limit.
    Each boat carries at most 2 people at the same time, provided the sum of
    the weight of those people is at most limit.
    Return the minimum number of boats to carry every given person.  (It is
    guaranteed each person can be carried by a boat.)
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


print(num_rescue_boats([1, 2], 3))  # 1
