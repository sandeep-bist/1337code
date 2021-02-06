from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        size, val = len(q), 0
        for _ in range(size):
            popped = q.popleft()
            val = popped.val
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        res.append(val)
    return res
        