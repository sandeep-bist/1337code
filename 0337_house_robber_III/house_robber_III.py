from typing import Tuple


class TreeNode:
    def __init__(self, x: int):
        """
        TreeNode constructor.
        """
        self.val = x
        self.left = None
        self.right = None


def rob_again_again(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return max(rob(root))


def rob(root: TreeNode) -> Tuple:
    if root is None:
        return (0, 0)
    left = rob(root.left)
    right = rob(root.right)
    now = root.val + left[1] + right[1]
    later = max(left) + max(right)
    return (now, later)
