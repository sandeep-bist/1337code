class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return 0
    return helper(root, 0)


def helper(root: TreeNode, curr: int):
    if not root:
        return float("inf")
    curr += 1
    if not root.left and not root.right:
        return curr
    return min(helper(root.left, curr), helper(root.right, curr))
