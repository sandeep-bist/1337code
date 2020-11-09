class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = 0
    def helper(node: TreeNode) -> int:
        nonlocal res
        if not node:
            return 0
        l, r = helper(node.left), helper(node.right)
        tilt = abs(l - r)
        res += tilt
        return l + node.val + r
    helper(root)
    return res