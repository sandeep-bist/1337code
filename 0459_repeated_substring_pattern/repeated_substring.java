class Solution {
    // Time: O(n)
    // Space: O(n)
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        int[] dp = new int[n];
        for (int i = 1; i < n; ++i) {
            int j = dp[i - 1];
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = dp[j - 1];
            }
            if (s.charAt(i) == s.charAt(j)) {
                ++j;
            }
            dp[i] = j;
        }
        int last = dp[n - 1];
        return last != 0 && n % (n - last) == 0;
    }

    // Time: O(n**2)
    // Space: O(n)
    public boolean repeatedSubstringPatternAlternate(String s) {
        return (s + s).substring(1, (s.length() * 2) - 1).contains(s);
    }
}