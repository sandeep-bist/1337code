class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxPower(String s) {
        int res = 1, count = 1;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                count++;
                res = Math.max(res, count);
            } else {
                count = 1;
            }
        }
        return res;
    }
}