class Solution {
    // Time: O(n)
    // Space: O(1)
    public char findTheDifference(String s, String t) {
        int n = s.length();
        char c = t.charAt(n);
        for (int i = 0; i < n; i++) {
            c ^= s.charAt(i) ^ t.charAt(i);
        }
        return c;
    }
}