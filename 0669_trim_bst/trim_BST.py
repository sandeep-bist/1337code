class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    def trim(node: TreeNode) -> TreeNode:
        if not node:
            return
        if node.val > high:
            return trim(node.left)
        if node.val < low:
            return trim(node.right)
        node.left = trim(node.left)
        node.right = trim(node.right)
        return node
    return trim(root)