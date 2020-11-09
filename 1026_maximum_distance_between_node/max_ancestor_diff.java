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
 
    // Time: O(n)
    // Space: O(n)
    public int maxAncestorDiff(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return helper(root, root.val, root.val);
    }
    
    private int helper(TreeNode node, int currMin, int currMax) {
        if (node == null) {
            return currMax - currMin;
        }
        currMin = Math.min(currMin, node.val);
        currMax = Math.max(currMax, node.val);
        int left = helper(node.left, currMin, currMax);
        int right = helper(node.right, currMin, currMax);
        return Math.max(left, right);
    }
}