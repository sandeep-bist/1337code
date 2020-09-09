class Solution {
    // Time: O(n)
    // Space: O(n)
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        int s = 0, t = 0;
        while (s < v1.length || t < v2.length) {
            Integer first = s < v1.length ? Integer.parseInt(v1[s++]) : 0;
            Integer second = t < v2.length ? Integer.parseInt(v2[t++]) : 0;
            if (first > second) {
                return 1;
            } else if (second > first) {
                return -1;
            }
        }
        return 0;
    }
}