// Time: O(n)
// Space: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0)
            return 0;
        int res = 0;
        int min = Integer.MAX_VALUE;
        for (int i: prices) {
            if (i < min) {
                min = i;
            }
            res = Math.max(res, i - min);
        }
        return res; 
    }
}