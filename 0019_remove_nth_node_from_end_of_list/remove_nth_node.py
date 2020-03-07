class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    hare = tort = head
    while n:
        hare = hare.next
        n -= 1
    if not hare:
        # Hare has reached end of list, will need to delete head.
        return head.next
    while hare.next:
        tort = tort.next
        hare = hare.next
    if tort.next:
        tort.next = tort.next.next
    return head
