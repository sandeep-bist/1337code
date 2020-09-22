class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head: 'Node', insertVal: int) -> 'Node':
    """
    Time: O(n)
    Space: O(1)
    """
    node = Node(insertVal, None)
    if not head:
        node.next = node
        return node
    curr = prev = head
    while True:
        prev = curr
        curr = curr.next
        if curr.val >= insertVal >= prev.val:
            break
        if prev.val > curr.val:
            if insertVal >= prev.val or insertVal <= curr.val:
                break
        if curr == head:
            break
    prev.next = node
    node.next = curr
    return head
