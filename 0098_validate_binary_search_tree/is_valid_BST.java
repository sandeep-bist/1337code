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
    // Space: O(1)
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }
    
    private boolean helper(TreeNode p, Integer low, Integer high) {
        if (p == null)  {
            return true;
        }
        if ((low != null && p.val <= low) || (high != null && p.val >= high)) {
            return false;
        }
        if (!helper(p.left, low, p.val) || !helper(p.right, p.val, high)) {
            return false;
        }
        return true;
    }
}