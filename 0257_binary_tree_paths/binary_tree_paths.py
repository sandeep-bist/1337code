from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree_paths(root: TreeNode) -> List[str]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    dfs(root, res, "")
    return res


def dfs(node: TreeNode, arr: List[str], curr: str):
    if not node:
        return True
    l = dfs(node.left, arr, curr + f"{node.val}->")
    r = dfs(node.right, arr, curr + f"{node.val}->")
    if l and r:
        arr.append(curr + str(node.val))
