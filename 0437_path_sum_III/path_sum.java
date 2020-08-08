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

// Time: O(n)
// Space: O(n)
class Solution {
    public int pathSum(TreeNode root, int sum) {
        HashMap<Integer, Integer> cache = new HashMap();
        return preorder(root, 0, sum, cache);
    }

    public int preorder(TreeNode root, int currSum, int target, HashMap<Integer, Integer> cache) {
        if (root == null)
            return 0;
        currSum += root.val;
        int res = cache.getOrDefault(currSum - target, 0);
        if (currSum == target)
            res++;
        cache.put(currSum, cache.getOrDefault(currSum, 0) + 1);
        res += preorder(root.left, currSum, target, cache) + preorder(root.right, currSum, target, cache);
        cache.put(currSum, cache.get(currSum) - 1);
        return res;
    }
}