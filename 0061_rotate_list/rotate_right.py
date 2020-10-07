class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    if not k or not head or not head.next:
        return head
    size = 1
    curr = head
    while curr.next:
        curr = curr.next
        size += 1
    curr.next = head
    start = end = head
    for _ in range(size - (k % size) - 1):
        end = end.next
    start = end.next
    end.next = None
    return start
