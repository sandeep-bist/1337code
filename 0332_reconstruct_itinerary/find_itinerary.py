from collections import defaultdict
from typing import List


def find_itinerary(tickets: List[List[str]]) -> List[str]:
    """
    Time: O(e * log(e/v)) where e is the number of edges
    Space: O(v + e)
    """
    targets = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []

    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
    visit('JFK')
    return route[::-1]
