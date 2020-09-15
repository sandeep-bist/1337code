class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def inorder_successor(node: 'Node') -> 'Node':
    """
    Time: O(log(n))
    Space: O(1)
    """
    curr = node
    if curr.right:
        curr = curr.right
        while curr.left:
            curr = curr.left
        return curr
    while curr.parent:
        curr = curr.parent
        if curr.val > node.val:
            return curr
