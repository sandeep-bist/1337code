from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(1)
    """
    prev, curr = None, head
    while curr:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next
    return prev