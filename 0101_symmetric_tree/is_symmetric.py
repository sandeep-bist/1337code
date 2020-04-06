from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return True
    d = deque([root.left, root.right])
    while d:
        n1, n2 = d.popleft(), d.popleft()
        if not n1 and not n2:
            continue
        if (not n1 or not n2) or n1.val != n2.val:
            return False
        d.extend([n1.left, n2.right, n1.right, n2.left])
    return True
