class Solution {
    // Time: O(log(m * n))
    // Space: O(1)
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) {
            return false;
        }
        int n = matrix[0].length;
        int i = 0, j = m * n;
        while (i < j) {
            int mid = (i + j) / 2;
            int midVal = matrix[mid / n][mid % n];
            if (midVal == target) {
                return true;
            }
            if (midVal < target) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        return false;
    }
}