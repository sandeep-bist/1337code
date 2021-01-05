class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    sent = ListNode(-1, head)
    pre = sent
    while head:
        if head.next and head.next.val == head.val:
            while head.next and head.next.val == head.val:
                head = head.next
            pre.next = head.next
        else:
            pre = pre.next
        head = head.next
    return sent.next