class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    tort = hare = head
    while hare and hare.next:
        tort = tort.next
        hare = hare.next.next
        if tort == hare:
            return True
    return False