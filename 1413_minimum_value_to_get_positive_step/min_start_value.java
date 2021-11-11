class Solution {
    // Time: O(n)
    // Space: O(1)
    public int minStartValue(int[] nums) {
        int min = 0, curr = 0;
        for (int i: nums) {
            curr += i;
            min = Math.min(min, curr);
        }
        return -min + 1;
    }
}