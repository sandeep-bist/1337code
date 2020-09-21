from typing import List


def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    buckets = [0] * 1001
    for p, start, end in trips:
        buckets[start] += p
        buckets[end] -= p
    passengers = 0
    for bucket in buckets:
        passengers += bucket
        if passengers > capacity:
            return False
    return True
