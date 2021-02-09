class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    total = 0
    def helper(node):
        nonlocal total
        if node:
            helper(node.right)
            total += node.val
            node.val = total
            helper(node.left)
        return node
    return helper(root)