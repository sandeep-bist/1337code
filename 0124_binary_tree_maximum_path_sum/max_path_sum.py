from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = [float('-inf')]
    helper(root, res)
    return res[0]


def helper(node: TreeNode, res: List[int]):
    if not node:
        return 0
    left = helper(node.left, res)
    right = helper(node.right, res)
    res[0] = max(res[0], left + node.val + right)
    return max(node.val + max(left, right), 0)
