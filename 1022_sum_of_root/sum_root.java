public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    private int sum = 0;

    // Time: O(n)
    // Space: O(1)
    public int sumRootToLeaf(TreeNode root) {
        dfs(root, 0);
        return sum;
    }

    private void dfs(TreeNode node, int currSum) {
        if (node == null) {
            return;
        }
        currSum = currSum << 1 | node.val;
        if (node.left == null && node.right == null) {
            sum += currSum;
        }
        dfs(node.left, currSum);
        dfs(node.right, currSum);
    }
}