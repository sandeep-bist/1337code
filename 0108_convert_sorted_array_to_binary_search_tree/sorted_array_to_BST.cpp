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
 * Time: O(n)
 * Space: O(n)
 */
TreeNode *sorted_array_to_BST(vector<int> &nums)
{
    return sorted_array_to_BST_helper(nums, 0, nums.size() - 1);
}

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