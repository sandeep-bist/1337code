class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_subtree(s: TreeNode, t: TreeNode) -> bool:
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    return in_order(t) in in_order(s)


def in_order(node: TreeNode) -> str:
    if not node:
        return "x"
    return f"({node.val}){in_order(node.left)}{in_order(node.right)}"
