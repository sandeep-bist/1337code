from typing import Tuple


class TreeNode:
    def __init__(self, x: int):
        """
        TreeNode constructor.
        """
        self.val = x
        self.left = None
        self.right = None


def rob_again_again(root: TreeNode) -> int:
    """
    The thief has found himself a new place for his thievery again. There is
    only one entrance to this area, called the "root." Besides the root, each
    house has one and only one parent house. After a tour, the smart thief
    realized that "all houses in this place forms a binary tree". It will
    automatically contact the police if two directly-linked houses were broken
    into on the same night.
    Determine the maximum amount of money the thief can rob tonight without
    alerting the police.
    """
    return max(rob(root))


def rob(root: TreeNode) -> Tuple:
    """
    Helper.
    """
    if root is None:
        return (0, 0)
    left = rob(root.left)
    right = rob(root.right)
    now = root.val + left[1] + right[1]
    later = max(left) + max(right)
    return (now, later)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n8.left = n10
n9.right = n11

print(rob_again_again(n1))  # 44
