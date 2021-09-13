class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxNumberOfBalloons(String text) {
        int[] strCount = count(text);
        int[] balloonCount = count("balloon");
        int res = text.length();
        for (char c : "balloon".toCharArray()) {
            res = Math.min(res, strCount[c - 'a'] / balloonCount[c - 'a']);
        }
        return res;
    }
    
    private int[] count(String str) {
        int[] res = new int[26];
        for (int i = 0; i < str.length(); i++) {
            res[str.charAt(i) - 'a']++;
        }
        return res;
    }
}