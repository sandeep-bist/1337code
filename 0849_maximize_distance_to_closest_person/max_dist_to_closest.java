class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxDistToClosest(int[] seats) {
        int res = 0, i = 0;
        int n = seats.length;
        while (i < n) {
            while (i < n && seats[i] == 1) {
                i++;
            }
            int j = i; // first pointer
            while (i < n && seats[i] == 0) {
                i++;
            }
            if (j == 0 || i == n) {
                res = Math.max(res, i - j);
            } else {
                res = Math.max(res, (i - j + 1) / 2);
            }
        }
        return res;
    }
}