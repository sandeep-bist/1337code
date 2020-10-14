class Solution {
    // Time: O(n)
    // Space: O(1)
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        return Math.max(robAgain(nums, 1, n - 1), robAgain(nums, 0, n - 2));
    }

    private int robAgain(int[] nums, int lo, int hi) {
        int prev = 0, curr = 0;
        for (int i = lo; i <= hi; i++) {
            int tmp = Math.max(curr, prev + nums[i]);
            prev = curr;
            curr = tmp;
        }
        return curr;
    }
}