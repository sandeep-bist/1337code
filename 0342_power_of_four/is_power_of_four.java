class Solution {
    // Time: O(1)
    // Space: O(1)
    public boolean isPowerOfFour(int num) {
        return num > 0 && (num & (num - 1)) == 0 && num % 3 == 1;
    }
}