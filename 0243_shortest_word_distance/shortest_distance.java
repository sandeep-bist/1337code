class Solution {
    // Time: O(n)
    // Space: O(1)
    public int shortestDistance(String[] words, String word1, String word2) {
        int minDistance = words.length;
        int x = -1, y = -1;
        for (int i = 0; i < words.length; i++) {
            String curr = words[i];
            if (curr.equals(word1)) {
                x = i;
            } else if (curr.equals(word2)) {
                y = i;
            }
            if (x != -1 && y != -1) {
                minDistance = Math.min(minDistance, Math.abs(x - y));
            }
        }
        return minDistance;
    }
}