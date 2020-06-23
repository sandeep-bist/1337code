class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: TreeNode) -> int:
    """
    Time: O(log**2(n)) or O(d**2) where d is the tree depth.
    Space: O(1)
    """
    if not root:
        return 0
    depth = find_depth(root)
    begin, end = (1 << depth), (1 << (depth+1)) - 1
    if path_exists(root, end):
        return end
    while begin + 1 < end:
        mid = (begin + end)//2
        if path_exists(root, mid):
            begin = mid
        else:
            end = mid
    return begin


def find_depth(root: TreeNode) -> int:
    depth = 0
    while root.left:
        root, depth = root.left, depth + 1
    return depth


def path_exists(root: TreeNode, num: int) -> bool:
    for s in bin(num)[3:]:
        if s == "0":
            root = root.left
        else:
            root = root.right
        if not root:
            return False
    return True
