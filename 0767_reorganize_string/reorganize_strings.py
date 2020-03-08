from collections import Counter
import heapq


def reorganize_string(S: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    pq = [(-y, x) for x, y in Counter(S).items()]
    heapq.heapify(pq)
    # to skip first iteration
    p_a, p_b = 0, ""
    while pq:
        a, b = heapq.heappop(pq)
        res += [b]
        if p_a < 0:
            # add previously popped item
            heapq.heappush(pq, (p_a, p_b))
        a += 1
        p_a, p_b = a, b
    res = "".join(res)
    return res if len(res) == len(S) else ""
