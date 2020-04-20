from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_from_preorder(preorder: List[int]) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    head = TreeNode(preorder[0])
    for i in preorder[1:]:
        insert(head, TreeNode(i))
    return head


def insert(node: TreeNode, new_node: TreeNode):
    if new_node.val > node.val:
        if not node.right:
            node.right = new_node
        else:
            insert(node.right, new_node)
    else:
        if not node.left:
            node.left = new_node
        else:
            insert(node.left, new_node)
