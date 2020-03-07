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
    Time: O(n)
    Space: O(n)
    """
    return sorted_array_to_BST_helper(nums, 0, len(nums) - 1)


def sorted_array_to_BST_helper(nums: List[int],
                               start: int, end: int) -> TreeNode:
    if start > end:
        return None
    mid = (start + end) // 2
    mid_node = TreeNode(nums[mid])
    mid_node.left = sorted_array_to_BST_helper(nums, start, mid - 1)
    mid_node.right = sorted_array_to_BST_helper(nums, mid + 1, end)
    return mid_node
