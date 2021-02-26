class Solution {
    // Time: O(n)
    // Space: O(1)
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int start = -1, end = -1;
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, nums[n - 1 - i]);
            max = Math.max(max, nums[i]);
            if (max > nums[i]) {
                end = i;
            }
            if (min < nums[n - 1 - i]) {
                start = n - 1 - i;               
            }
        }
        if (start == -1) { // array is already sorted
            return 0;
        }
        return end - start + 1;
    }
}