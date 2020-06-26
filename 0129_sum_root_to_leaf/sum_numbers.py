class TreeNode:
    def __init__(self, val=0, left=None,
                 right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    return dfs(root, 0)


def dfs(node: TreeNode, curr: int) -> int:
    if node:
        curr = curr * 10 + node.val
        if not node.left and not node.right:
            return curr
        return dfs(node.left, curr) + dfs(node.right, curr)
    return 0
