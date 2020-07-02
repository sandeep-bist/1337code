from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    res = deque()
    q = [root]
    while q:
        tmp, level = [], []
        for node in q:
            level.append(node.val)
            node.left and tmp.append(node.left)
            node.right and tmp.append(node.right)
        res.appendleft(level)
        q = tmp
    return res
