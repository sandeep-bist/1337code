import java.util.HashMap;

class Solution {
    // Time: O(n)
    // Space: O(n)
    public boolean wordPattern(String pattern, String str) {
        HashMap<Character, String> map = new HashMap<Character, String>();
        String[] split = str.split(" ");
        if (split.length != pattern.length()) {
            return false;
        }
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String w = split[i];
            if (!map.containsKey(c)) {
                if (map.containsValue(w)) {
                    return false;
                }
            } else {
                if (!map.get(c).equals(w)) {
                    return false;
                }
            }
            map.put(c, w);
        }
        return true;
    }
}