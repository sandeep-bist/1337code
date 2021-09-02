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
    // Time: O(C0+C1+...+CN) where CN is the Catalan number
    // Space: O(n * Cn)
    public List<TreeNode> generateTrees(int n) {
        return generate(1, n);
    }
    
    private List<TreeNode> generate (int start, int end) {
        List<TreeNode> list = new ArrayList<TreeNode>(); 
        if (start > end) {
            list.add(null);
        }
        for(int idx = start; idx <= end; idx++) {
            List<TreeNode> leftList = generate(start, idx - 1);
            List<TreeNode> rightList = generate(idx + 1, end);
            for (TreeNode left : leftList) {
                for(TreeNode right: rightList) {
                    TreeNode root = new TreeNode(idx);
                    root.left = left;
                    root.right = right;
                    list.add(root);
                }
            }
        }
        return list;
    }
}