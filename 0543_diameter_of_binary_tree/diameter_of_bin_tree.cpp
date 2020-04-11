#include <iostream>
#include <algorithm>

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
 * Space: O(1)
 */
int diameter_of_binary_tree(TreeNode *root)
{
    int m = 0;
    depth(root, &m);
    return m;
}

int depth(TreeNode *node, int *m)
{
    if (!node)
        return 0;
    int left = depth(node->left, m);
    int right = depth(node->right, m);
    *m = max(left + right, *m);
    return max(left, right) + 1;
}
