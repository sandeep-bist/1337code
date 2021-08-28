class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean canJump(int[] nums) {
        int maxJumpPos = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i > maxJumpPos) {
                return false;
            }
            maxJumpPos = Math.max(maxJumpPos, nums[i] + i);
            if (maxJumpPos >= n - 1) {
                return true;
            }
        }
        return true;
    }
}