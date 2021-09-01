class Solution {
    // Time: O(n)
    // Space: O(1)
    public int arrayNesting(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            while (nums[i] != -1) {
                int tmp = nums[i];
                nums[i] = -1;
                i = tmp;
                count++;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}