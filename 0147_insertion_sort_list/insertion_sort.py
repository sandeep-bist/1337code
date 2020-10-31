class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: ListNode) -> ListNode:
    """
    Time: O(n**2)
    Space: O(1)
    """
    s = ListNode()
    while head:
        left, right = s, s.next
        while right:
            if head.val < right.val:
                break
            left, right = right, right.next
        _next = head.next
        left.next = head
        head.next = right
        head = _next
    return s.next
        