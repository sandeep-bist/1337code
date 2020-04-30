from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right


def is_valid_sequence(root: TreeNode, arr: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    return dfs(root, 0, arr)


def dfs(node: TreeNode, index: int, arr: List[int]):
    if not node or index >= len(arr) or arr[index] != node.val:
        return False
    if not node.left and not node.right:
        return len(arr) == index + 1
    return (dfs(node.left, index + 1, arr) or
            dfs(node.right, index + 1, arr))
