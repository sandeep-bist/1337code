class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    return helper(root)
    

def helper(node: TreeNode, MIN = None, MAX = None):
    if not node:
        return True
    if (MAX != None and node.val >= MAX) or (MIN != None and node.val <= MIN):
        return False
    if not helper(node.left, MIN, node.val) or not helper(node.right, node.val, MAX):
        return False
    return True