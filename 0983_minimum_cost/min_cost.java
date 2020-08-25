class Solution {
    // Time: O(m) where m is the max travel date
    // Space: O(m)
    public int mincostTickets(int[] days, int[] costs) {
        int lastDay = days[days.length - 1];
        boolean[] isTravelDay = new boolean[lastDay + 1];
        int[] dp = new int[lastDay + 1];
        for (int day : days) {
            isTravelDay[day] = true;
        }
        for (int i = 1; i <= lastDay; i++) {
            if (!isTravelDay[i]) {
                dp[i] = dp[i - 1];
                continue;
            }
            dp[i] = dp[i - 1] + costs[0];
            dp[i] = Math.min(dp[i >= 7 ? i - 7 : 0] + costs[1], dp[i]);
            dp[i] = Math.min(dp[i >= 30 ? i - 30 : 0] + costs[2], dp[i]);
        }
        return dp[lastDay];
    }
}