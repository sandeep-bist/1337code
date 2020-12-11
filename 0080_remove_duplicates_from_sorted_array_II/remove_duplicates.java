class Solution {
    // Time: O(n)
    // Space: O(1)
    public int removeDuplicates(int[] nums) {
        int j = 0;
        for (int i: nums) {
            if (j < 2 || nums[j - 2] < i) {
                nums[j++] = i;
            }
        }
        return j;
    }
}
