class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    return serialize(p) == serialize(q)


def serialize(node: TreeNode) -> bool:
    if not node:
        return "x"
    return str(node.val) + serialize(node.left) + serialize(node.right)
