class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxProduct(int[] nums) {
        int maxSoFar = nums[0], minSoFar = nums[0], res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            int tmp = Math.max(curr, Math.max(maxSoFar * curr, minSoFar * curr));
            minSoFar = Math.min(curr, Math.min(maxSoFar * curr, minSoFar * curr));
            maxSoFar = tmp;
            res = Math.max(res, maxSoFar);
        }
        return res;
    }
}