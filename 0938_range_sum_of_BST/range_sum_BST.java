public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    
    int res = 0;
    int low;
    int high;
    
    // Time: O(n)
    // Space: O(n)
    public int rangeSumBST(TreeNode root, int low, int high) {
        this.low = low;
        this.high = high;
        dfs(root);
        return res;
    }
    
    private void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.val >= low && node.val <= high) {
            res += node.val;
        }
        if (node.val > low) {
            dfs(node.left);
        }
        if (node.val < high) {
            dfs(node.right);
        }
    }
}