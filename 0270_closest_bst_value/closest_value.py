class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root: TreeNode, target: float) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    res = root.val
    while root:
        if abs(root.val - target) < abs(res - target):
            res = root.val
        root = root.left if target < root.val else root.right
    return res
