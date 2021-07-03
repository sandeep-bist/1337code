class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        int j = nums.length;
        while (i < j) {
            int mid = (i + j) / 2;
            int midVal = nums[mid];
            if (midVal == target) {
                return mid;
            }
            if (midVal > target) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        return i;
    }
}
