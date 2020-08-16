// Time: O(n)
// Space: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MAX_VALUE, buy2 = Integer.MAX_VALUE;
        int sell1 = 0, sell2 = 0;
        for (int i : prices) {
            buy1 = Math.min(buy1, i);
            sell1 = Math.max(sell1, i - buy1);
            buy2 = Math.min(buy2, i - sell1);
            sell2 = Math.max(sell2, i - buy2);
        }
        return sell2;
    }
}