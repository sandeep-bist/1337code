class Solution {
    // Time: O(n)
    // Space: O(1)
    public int lengthOfLastWord(String s) {
        int res = 0, p = s.length() - 1;
        while (p >= 0) {
            if (s.charAt(p) != ' ') {
                res++;
            } else if (res > 0) {
                return res;
            }
            p--;
        }
        return res;
    }
}
