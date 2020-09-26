class Solution {
    // Time: O(n)
    // Space: O(1)
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.length == 0) {
            return 0;
        }
        int res = 0;
        for (int i = 0; i < timeSeries.length - 1; i++) {
            res += Math.min(timeSeries[i + 1] - timeSeries[i], duration);
        }
        return res + duration;
    }
}