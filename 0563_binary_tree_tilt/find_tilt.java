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
    
    int res;
    
    // Time: O(n)
    // Space: O(n)
    public int findTilt(TreeNode root) {
        res = 0;
        helper(root);
        return res;
    }
    
    private int helper(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int l = helper(node.left);
        int r = helper(node.right);
        int tilt = Math.abs(l - r);
        res += tilt;
        return l + node.val + r;
    }
}