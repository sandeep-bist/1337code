class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: ListNode) -> ListNode:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    if not head or not head.next:
        return head
    mid = get_mid(head)
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)


def get_mid(head: ListNode) -> ListNode:
    mid_prev = head
    head = head.next
    while head and head.next:
        mid_prev = mid_prev.next
        head = head.next.next
    mid = mid_prev.next
    mid_prev.next = None
    return mid


def merge(first: ListNode, sec: ListNode) -> ListNode:
    if not first or not sec:
        return first or sec
    sentinel = ListNode()
    tail = sentinel
    while first and sec:
        if first.val < sec.val:
            tail.next = first
            first = first.next
        else:
            tail.next = sec
            sec = sec.next
        tail = tail.next
    tail.next = first if first else sec
    return sentinel.next
