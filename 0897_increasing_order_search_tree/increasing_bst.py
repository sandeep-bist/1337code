class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def increasingBST(root: TreeNode, tail = None) -> TreeNode:
    """
    Time: O(n)
    Space: O(h) where h is the height of the tree
    """
    if not root:
        return tail
    res = increasingBST(root.left, root)
    root.left = None
    root.right = increasingBST(root.right, tail)
    return res