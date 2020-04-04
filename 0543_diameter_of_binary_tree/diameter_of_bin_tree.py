from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    diameter = [0]
    depth(root, diameter)
    return diameter[0]


def depth(root: TreeNode, d: List[int]) -> int:
    if not root:
        return 0
    left = depth(root.left, d)
    right = depth(root.right, d)
    d[0] = max(d[0], left + right)
    return 1 + max(left, right)
