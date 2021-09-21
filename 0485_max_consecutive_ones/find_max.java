class Solution {
    // Time: O(n)
    // Space: O(1)
    public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0, curr = 0;
        for (int num: nums) {
            if (num == 1) {
                curr++;
                res = Math.max(res, curr);
            } else {
                curr = 0;
            }
        }
        return res;
    }
}