#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

/**
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 */
bool isValidBST(TreeNode* root) {
    return helper(root, NULL, NULL);
}

/**
 * Helper func. 
 */
bool helper(TreeNode* node, int* min, int* max)
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