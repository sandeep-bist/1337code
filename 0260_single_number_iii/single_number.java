class Solution {
    // Time: O(n)
    // Space: O(1)
    public int[] singleNumber(int[] nums) {
        int bitmask = 0;
        for (int num : nums) {
            bitmask ^= num;
        }
        int diff = bitmask & (-bitmask);
        int[] res = {0, 0};
        for (int num: nums) {
            if ((num & diff) == 0) {
                res[0] ^= num;
            } else {
                res[1] ^= num;
            }
        }
        return res;
    }
}