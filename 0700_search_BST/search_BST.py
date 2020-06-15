class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_BST(root: TreeNode, val: int) -> TreeNode:
    """
    Time: O(log(n))
    Space: O(1)
    """
    if not root:
        return None
    if val == root.val:
        return root
    if val > root.val:
        return search_BST(root.right, val)
    return search_BST(root.left, val)
