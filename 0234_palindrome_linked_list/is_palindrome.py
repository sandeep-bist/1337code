class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_palindrome(head: ListNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    t = h = head
    while h and h.next:
        stack.append(t.val)
        h = h.next.next
        t = t.next
    if h:
        t = t.next
    while t:
        if t.val != stack.pop():
            return False
        t = t.next
    return True
