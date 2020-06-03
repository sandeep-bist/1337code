class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    """
    Time: O(1)
    Space: O(1)
    """
    _next = node.next
    node.val = _next.val
    node.next = _next.next
