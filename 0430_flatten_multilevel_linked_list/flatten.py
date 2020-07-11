class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':
    """
    Time: O(n)
    Space: O(n)
    """
    if not head:
        return
    s = Node(0, None, None, None)
    prev = s
    stack = [head]
    while stack:
        curr = stack.pop()
        curr.prev = prev
        prev.next = curr
        if curr.next:
            stack.append(curr.next)
            curr.next = None
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr
    s.next.prev = None
    return s.next
