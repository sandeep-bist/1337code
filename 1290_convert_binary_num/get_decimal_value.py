class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = ""
    while head:
        res += str(head.val)
        head = head.next
    return int(res, 2)