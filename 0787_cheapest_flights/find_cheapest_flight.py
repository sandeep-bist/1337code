from collections import defaultdict
from heapq import heappush, heappop
from typing import List


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
    Time: O(n**2 * log(n))
    Space: O(n**2)
    """
    graph = defaultdict(list)
    for c1, c2, edge in flights:
        graph[c1].append((edge, c2))
    pq = [(0, K, src)]
    while pq:
        cost, stops, city = heappop(pq)
        if city == dst:
            return cost
        if stops >= 0:
            for n_cost, n_city in graph[city]:
                heappush(pq, (cost + n_cost, stops - 1, n_city))
    return -1
