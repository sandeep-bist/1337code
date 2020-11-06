class Solution {
    
    int[] nums;
    int threshold;
    
    // Time: O(log(n))
    // Space: O(1)
    public int smallestDivisor(int[] nums, int threshold) {
        this.nums = nums;
        this.threshold = threshold;
        int i = 1, j = nums[nums.length - 1];
        while (i < j) {
            int mid = (i + j) / 2;
            if (isUnderThreshold(mid)) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        return i;
    }
    
    private boolean isUnderThreshold(int mid) {
        int total = 0;
        for (int i: nums) {
            total += (i + mid - 1) / mid;
        }
        return total <= threshold;
    }
}