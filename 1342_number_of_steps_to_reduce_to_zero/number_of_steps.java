class Solution {
    // Time: O(1)
    // Space: O(1)
    public int numberOfSteps (int num) {
        if (num == 0) {
            return 0;
        }
        int res = 0;
        while (num != 0) {
            res += ((num & 1) == 0 ? 1 : 2);
            num >>= 1;
                
        }
        return res - 1;
    }
}