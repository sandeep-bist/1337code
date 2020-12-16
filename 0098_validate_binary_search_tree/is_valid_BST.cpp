#include <iostream>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

/**
 * Time: O(n)
 * Space: O(n)
 */
bool is_valid_bst(TreeNode *root)
{
    return helper(root, NULL, NULL);
}

bool helper(TreeNode *node, int *min, int *max)
{
    if (!node)
        return true;
    if ((max && node->val >= *max) || (min && node->val <= *min))
        return false;
    if (!helper(node->left, min, &node->val) ||
        !helper(node->right, &node->val, max))
        return false;
    return true;
}