class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean carPooling(int[][] trips, int capacity) {
        int[] buckets = new int[1001];
        for (int[] trip : trips) {
            buckets[trip[1]] += trip[0];
            buckets[trip[2]] -= trip[0];
        }
        int passengers = 0;
        for (int bucket : buckets) {
            passengers += bucket;
            if (passengers > capacity) {
                return false;
            }
        }
        return true;
    }
}