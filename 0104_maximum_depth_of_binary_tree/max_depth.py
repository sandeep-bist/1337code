class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if root is None: 
        return 0 
    else: 
        left_height = maxDepth(root.left) 
        right_height = maxDepth(root.right) 
        return max(left_height, right_height) + 1 