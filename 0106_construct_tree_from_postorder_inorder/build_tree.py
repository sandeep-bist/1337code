from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    m = {index: v for v, index in enumerate(inorder)}

    def helper(lo: int, hi: int):
        if lo > hi:
            return
        new_node = TreeNode(postorder.pop())
        index = m.get(new_node.val)
        new_node.right = helper(index + 1, hi)
        new_node.left = helper(lo, index - 1)
        return new_node
    return helper(0, len(postorder) - 1)
