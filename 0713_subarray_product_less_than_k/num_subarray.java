class Solution {
    // Time: O(n)
    // Space: O(1)
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) {
            return 0;
        }
        int res = 0, l = 0, p = 1;
        for (int i = 0; i < nums.length; i++) {
            p *= nums[i];
            while (p >= k) {
                p /= nums[l++];
            }
            res += i - l + 1;
        }
        return res;
    }
}