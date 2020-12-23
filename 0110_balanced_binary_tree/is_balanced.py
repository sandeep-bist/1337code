class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    return dfs(root) != -1
    
def dfs(node: TreeNode) -> int:
    if not node:
        return 0
    left = dfs(node.left)
    if left == -1:
        return -1
    right = dfs(node.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left, right) + 1