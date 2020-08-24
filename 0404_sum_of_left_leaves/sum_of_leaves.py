class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(self, root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return helper(root, 1)


def helper(node: TreeNode, side: bool) -> int:
    if not node:
        return 0
    if not node.right and not node.left:
        return node.val if side == 0 else 0
    return helper(node.left, 0) + helper(node.right, 1)
