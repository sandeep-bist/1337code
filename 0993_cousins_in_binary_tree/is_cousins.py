from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_cousins(root: TreeNode, x: int, y: int) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    q = deque([root])
    while q:
        siblings = cousins = False
        size = len(q)
        for _ in range(size):
            popped = q.popleft()
            if not popped:
                siblings = False
            else:
                if popped.val == x or popped.val == y:
                    if not cousins:
                        siblings = cousins = True
                    else:
                        return not siblings
                q.append(popped.left) if popped.left else None
                q.append(popped.right) if popped.right else None
                q.append(None)
        if cousins:
            return False
    return False
