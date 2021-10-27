class Solution {
    // Time: O(n)
    // Space: O(1)
    public void sortColors(int[] nums) {
        int c = 0, c0 = 0;
        int c2 = nums.length - 1;
        while (c <= c2) {
            if (nums[c] == 0) {
                swap(nums, c, c0);
                c++;
                c0++;
            } else if (nums[c] == 1) {
                c++;
            } else {
                swap(nums, c, c2);
                c2--;
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}