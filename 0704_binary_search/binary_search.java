class Solution {
    // Time: O(log(n))
    // Space: (1)
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1;
        while (i <= j) {
            int mid = (i + j) / 2;
            int val = nums[mid];
            if (val == target) {
                return mid;
            }
            if (target < val) {
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        }
        return -1;
    }
}