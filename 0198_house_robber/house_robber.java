class Solution {
    // Time: O(n)
    // Space: O(1)
    public int rob(int[] nums) {
        int prev = 0, curr = 0;
        for (int num : nums) {
            int tmp = Math.max(num + prev, curr);
            prev = curr;
            curr = tmp;
        }
        return curr;
    }
}