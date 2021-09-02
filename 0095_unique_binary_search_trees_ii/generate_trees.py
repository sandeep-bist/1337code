from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n: int) -> List[Optional[TreeNode]]:
    """
    Time: O(C0+C1+...+CN) where CN is the Catalan number
    Space: O(n * Cn)
    """
    return generate(1, n)

def generate(start: int, end: int) -> List[Optional[TreeNode]]:
    arr = []
    if start > end:
        arr.append(None)
    for i in range(start, end + 1):
        left_arr = generate(start, i - 1)
        right_arr = generate(i + 1, end)
        for left in left_arr:
            for right in right_arr:
                root = TreeNode(i)
                root.left = left
                root.right = right
                arr.append(root)
    return arr