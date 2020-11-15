class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = 0
    def helper(node: TreeNode):
        nonlocal res
        if not node:
            return
        if high >= node.val >= low:
            res += node.val
        if node.val > low:
            helper(node.left)
        if node.val < high:
            helper(node.right)
    helper(root)
    return res