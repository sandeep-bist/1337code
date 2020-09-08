from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf(self, root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    sum_of_nodes = [0]
    dfs(root, 0, sum_of_nodes)
    return sum_of_nodes[0]


def dfs(node: TreeNode, curr: int, sum_of_nodes: List[int]):
    if not node:
        return
    curr = curr << 1 | node.val
    if not node.left and not node.right:
        sum_of_nodes[0] += curr
    dfs(node.left, curr, sum_of_nodes)
    dfs(node.right, curr, sum_of_nodes)
