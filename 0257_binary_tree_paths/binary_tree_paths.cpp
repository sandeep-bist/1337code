#include <iostream>
#include <string>
#include <vector>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

vector<string> binaryTreePaths(TreeNode *root)
{
    vector<string> res;
    if (!root)
        return res;
    dfs(root, res, "");
    return res;
}

/**
 * Time: O(n)
 * Space: O(n) 
 */
void dfs(TreeNode *node, vector<string> &arr, string curr)
{
    if (!node->left && !node->right)
    {
        curr += to_string(node->val);
        arr.push_back(curr);
        return;
    }
    curr += to_string(node->val) + "->";
    if (node->left)
        dfs(node->left, arr, curr);
    if (node->right)
        dfs(node->right, arr, curr);
}
