class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean increasingTriplet(int[] nums) {
        int small = Integer.MAX_VALUE, big = Integer.MAX_VALUE;
        for (int n : nums) {
            if (n <= small) {
                small = n;
            }
            else if (n <= big) {
                big = n;
            }
            else {
                return true;
            }
        }
        return false;
    }
}