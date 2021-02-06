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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(res, root, 0);
        return res;
    }
    
    private void dfs(List<Integer> res, TreeNode node, int currDepth) {
        if (node == null) {
            return;
        }
        if (currDepth == res.size()) {
            res.add(node.val);   
        }
        dfs(res, node.right, currDepth + 1);
        dfs(res, node.left, currDepth + 1);
    }
}