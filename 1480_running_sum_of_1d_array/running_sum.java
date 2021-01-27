class Solution {
    // Time: O(n)
    // Space: O(n)
    public int[] runningSum(int[] nums) {
        int n = nums.length, tmp = 0;
        int[] res = new int[nums.length];
        for (int i = 0; i < n; i++) {
            tmp += nums[i];
            res[i] = tmp;
        }
        return res;
    }
}