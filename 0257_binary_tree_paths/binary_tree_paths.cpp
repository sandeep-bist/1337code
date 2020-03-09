#include <iostream>
#include <string>
#include <vector>

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
vector<string> binary_tree_paths(TreeNode *root)
{
    vector<string> res;
    if (!root)
        return res;
    dfs(root, res, "");
    return res;
}

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
