class Solution {
    public int arrangeCoins(int n) {
        // Time: O(log(n))
        // Space: O(1)
        long nn = (long)n;
        long start = 0, end = nn;
        while (start <= end) {
            long mid = start + (end - start) / 2;
            if (gaussSum(mid, mid + 1) <= nn) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return (int)(start - 1);
    }
    
    private long gaussSum(long pairs, long sumOfPairs) {
        return pairs * sumOfPairs / 2;
    }
}