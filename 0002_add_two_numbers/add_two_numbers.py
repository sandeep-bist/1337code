class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    return add_two_numbers_helper(l1, l2, 0)


def add_two_numbers_helper(l1: ListNode, l2: ListNode,
                           carry: int = 0) -> ListNode:
    if not l1 and not l2 and not carry:
        return None
    total = carry
    if l1:
        total += l1.val
        l1 = l1.next
    if l2:
        total += l2.val
        l2 = l2.next
    carry = 1 if total >= 10 else 0
    new_node = ListNode(total % 10)
    new_node.next = add_two_numbers_helper(l1, l2, carry)
    return new_node
