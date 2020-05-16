class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    odd = odd_head = ListNode(-1)
    even = even_head = ListNode(-1)
    while head:
        odd.next = head
        odd = odd.next
        even.next = head.next
        even = even.next
        head = head.next.next if head.next else None
    odd.next = even_head.next
    return odd_head.next
