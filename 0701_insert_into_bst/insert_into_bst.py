class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    """
    Time: O(log(n))
    Space: O(1)
    """
    if not root:
        return TreeNode(val)
    if root.val < val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    return root
