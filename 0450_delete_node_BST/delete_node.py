class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: TreeNode, key: int) -> TreeNode:
    """
    Time: O(log(n))
    Space: O(h) where h is the height of the tree
    """
    if not root:
        return
    if key > root.val:
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    else:
        if not root.left and not root.right:
            root = None
        elif root.right:
            root.val = successor(root, root.val)
            root.right = self.deleteNode(root.right, root.val)
        else:
            root.val = predecessor(root, root.val)
            root.left = self.deleteNode(root.left, root.val)
    return root


def successor(node: TreeNode) -> int:
    node = node.right
    while node.left:
        node = node.left
    return node.val


def predecessor(node: TreeNode) -> int:
    node = node.left
    while node.right:
        node = node.right
    return node.val
