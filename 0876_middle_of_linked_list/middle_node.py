class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middle_node(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    t = h = head
    while h and h.next:
        h = h.next.next
        t = t.next
    return t
