class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) {
            return m * n;
        }
        int row = m, col = n;
        for (int i = 0; i < ops.length; i++) {
            row = Math.min(row, ops[i][0]);
            col = Math.min(col, ops[i][1]);
        }
        return row * col;
    }
}