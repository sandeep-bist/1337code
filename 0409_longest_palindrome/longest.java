// Time: O(n)
// Space: O(1)
class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[128];
        int res = 0;
        for (char c : s.toCharArray()) {
            count[c] += 1;
            if (count[c] == 2) {
                res += 2;
                count[c] = 0;
            }
        }
        return res == s.length() ? res : res + 1;
    }
}