class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    h = t = head
    while h and h.next:
        t = t.next
        h = h.next.next
        if h == t:
            t = head
            while t != h:
                t = t.next
                h = h.next
            return t
