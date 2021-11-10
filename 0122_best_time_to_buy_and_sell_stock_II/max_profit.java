class Solution {
    public int maxProfit(int[] prices) {
        // Time: O(n)
        // Space: O(1)
        int res = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
}