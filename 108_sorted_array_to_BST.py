from typing import List


class TreeNode:
    def __init__(self, x):
        """
        TreeNode constructor.
        """
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_BST(nums: List[int]) -> TreeNode:
    """
    Given an array where elements are sorted in ascending order, convert it
    to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary
    tree in which the depth of the two subtrees of every node never differ
    by more than 1.
    """
    return sorted_array_to_BST_helper(nums, 0, len(nums) - 1)


def sorted_array_to_BST_helper(nums: List[int],
                               start: int, end: int) -> TreeNode:
    """
    Helper.
    """
    if start > end:
        return None
    mid = (start + end) // 2
    mid_node = TreeNode(nums[mid])
    mid_node.left = sorted_array_to_BST_helper(nums, start, mid - 1)
    mid_node.right = sorted_array_to_BST_helper(nums, mid + 1, end)
    return mid_node


"""
[-10, -3, 0, 5, 9]

      0
     / \
   -3   9
   /   /
 -10  5
"""
