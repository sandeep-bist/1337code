from heapq import heapify, heappush, heappop
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    """
    Merge k sorted linked lists and return it as one sorted list.
    """
    h = [(l.val, id(l), l) for l in lists if l]
    heapify(h)
    head = cur = ListNode(None)
    while h:
        val, node_id, node = heappop(h)
        cur.next = node
        cur = cur.next
        node = node.next
        if node:
            heappush(h, (node.val, id(node), node))
    return head.next


def print_linked_list(head: ListNode):
    """
    Prints a linked list.
    """
    while head:
        print(head.val)
        head = head.next


if __name__ == "main":
    list_a = ListNode(1)
    list_a.next = ListNode(4)
    list_a.next.next = ListNode(5)

    list_b = ListNode(1)
    list_b.next = ListNode(3)
    list_b.next.next = ListNode(4)

    list_c = ListNode(2)
    list_c.next = ListNode(6)

    arr = [
        list_a,  # 1->4->5
        list_b,  # 1->3->4,
        list_c   # 2->6
    ]

    print_linked_list(merge_k_lists(arr))
    # 1->1->2->3->4->4->5->6
