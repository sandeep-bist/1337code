from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_elements(root1: TreeNode, root2: TreeNode) -> List[int]:
    """
    Time: O(n + m)
    Space: O(n + m)
    """
    return merge(in_order(root1), in_order(root2))


def in_order(node: TreeNode):
    return (in_order(node.left) + [node.val] + in_order(node.right)) if node else []


def merge(m: List[int], n: List[int]):
    res = []
    i = j = 0
    while i < len(m) and j < len(n):
        if m[i] <= n[j]:
            res.append(m[i])
            i += 1
        else:
            res.append(n[j])
            j += 1
    while i < len(m):
        res.append(m[i])
        i += 1
    while j < len(n):
        res.append(n[j])
        j += 1
    return res
