#include <iostream>
#include <vector>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x)
    {
        val = x;
        left = NULL;
        right = NULL;
    }
};

/**
 * Given an array where elements are sorted in ascending order, convert it
 * to a height balanced BST.
 * For this problem, a height-balanced binary tree is defined as a binary
 * tree in which the depth of the two subtrees of every node never differ
 * by more than 1. 
 */
TreeNode *sorted_array_to_BST(vector<int> &nums)
{
    return sorted_array_to_BST_helper(nums, 0, nums.size() - 1);
}

/**
 * Helper. 
 */
TreeNode *sorted_array_to_BST_helper(vector<int> &nums, int start, int end)
{
    if (start > end)
        return NULL;
    int mid = (start + end) / 2;
    TreeNode *mid_node = new TreeNode(nums[mid]);
    mid_node->left = sorted_array_to_BST_helper(nums, start, mid - 1);
    mid_node->right = sorted_array_to_BST_helper(nums, mid + 1, end);
    return mid_node;
}

/*
[-10, -3, 0, 5, 9]

      0
     / \
   -3   9
   /   /
 -10  5
*/