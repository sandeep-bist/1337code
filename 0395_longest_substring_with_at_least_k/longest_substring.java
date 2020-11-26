public class Solution {
    // Time: O(n)
    // Space: O(n)
    public int longestSubstring(String s, int k) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        char[] chars = new char[26];
        for (int i = 0; i < s.length(); i += 1) {
            chars[s.charAt(i) - 'a'] += 1;
        }
        boolean flag = true;
        for (int i = 0; i < chars.length; i += 1) {
            if (chars[i] < k && chars[i] > 0) {
                flag = false;
            }
        }
        if (flag == true) {
            return s.length();
        }
        
        int res = 0;
        int start = 0, cur = 0;
        // otherwise we use all the infrequent elements as splits
        while (cur < s.length()) {
            if (chars[s.charAt(cur) - 'a'] < k) {
                res = Math.max(res, longestSubstring(s.substring(start, cur), k));
                start = cur + 1;
            }
            cur++;
        }
        res = Math.max(res, longestSubstring(s.substring(start), k));
        return res;
    }
}