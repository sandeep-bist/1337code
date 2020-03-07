from heapq import heapify, heappush, heappop
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    """
    Time: O(k * n * log(n))
    Space: O(k * n)
    """
    h = [(l.val, id(l), l) for l in lists if l]
    heapify(h)
    head = cur = ListNode(None)
    while h:
        _, __, node = heappop(h)
        cur.next = node
        cur = cur.next
        node = node.next
        if node:
            heappush(h, (node.val, id(node), node))
    return head.next