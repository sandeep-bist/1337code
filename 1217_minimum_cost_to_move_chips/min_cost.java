class Solution {
    public int minCostToMoveChips(int[] position) {
        // Time: O(n)
        // Space: O(1)
        int odd = 0, even = 0;
        for (int pos: position) {
            if (pos % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        return Math.min(even, odd);
    }
}