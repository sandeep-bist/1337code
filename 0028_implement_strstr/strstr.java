class Solution {
    // Time: O(n)
    // Space: O(n)
    public int strStr(String s, String t) {
        int[] prefix = kmp(t);
        int i, j;
        for (i = 0, j = 0; i < s.length() && j < t.length(); i++) {
            while (j > 0 && s.charAt(i) != t.charAt(j)) {
                j = prefix[j - 1];
            }
            if (s.charAt(i) == t.charAt(j)) {
                j++;
            }
        }
        return j == t.length() ? i - j : -1;
    }

    private int[] kmp(String s) {
        int[] prefix = new int[s.length()];
        for (int i = 1, j = 0; i < s.length(); i++) {
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = prefix[j - 1];
            }
            if (s.charAt(i) == s.charAt(j)) {
                j++;
            }
            prefix[i] = j;
        }
        return prefix;
    }
}