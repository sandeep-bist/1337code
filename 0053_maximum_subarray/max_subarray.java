class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxSubArray(int[] nums) {
        if (nums.length == 0)
            return 0;
        int maxSoFar = nums[0], maxCurr = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            maxCurr = Math.max(curr, maxCurr + curr);
            maxSoFar = Math.max(maxCurr, maxSoFar);
        }
        return maxSoFar;
    }
}